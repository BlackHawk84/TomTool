#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import datetime
import logging
import os
import re
import subprocess
import time
from PyQt4 import QtGui, QtCore
from contextlib import closing

import bcrypt
import grin

from TomTool.DBClient import Test3Client, ActivitiClient
from TomTool.Generated.main_window import Ui_MainWindow
from TomTool.lib import xmlrpc_client, rpyc_client


class CTomToolMainWindow(QtGui.QMainWindow):

    serverXMLRPC = 'http://127.0.0.1:8881'
    rpyc_port = 18861
    rpyc_host = "localhost"

    def __init__(self, conf='tomtool.ini'):
        super(CTomToolMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # region Configuration file
        config = ConfigParser.ConfigParser()
        config.read(conf)

        self._connectionsdir = config.get('Connections', "dir")
        self._connections = config.get('Connections', "connections")
        self._localsshFS = config.get('Connections', "localsshFS")
        self._remotesshFS = config.get('Connections', "remotesshFS")

        self._restartscript = config.get('Scripts', "restartscript")
        autoupdate_interval = config.getint('Autoupdate', 'interval')
        # endregion

        self.proxy = xmlrpc_client.xmlrpc_client(CTomToolMainWindow.serverXMLRPC)

        # Timer for the automatic status update
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(autoupdate_interval)
        self.timer.timeout.connect(self.update_status)

        self.rpyc_connected = False

        self.logger = logging.getLogger("TomTool")
        self.logger.info('Tom Tool initialization')

        self.connection_data = []
        self.palette = {
            'IN_CYCLE': 'QLabel {color: green ; font: bold}',

            'ALARM': 'QLabel {color: red; font: bold}',
            'EMERGENCY': 'QLabel {color: red; font: bold}',

            'RESTORING': 'QLabel {color: orange ; font: bold}',
            'READY_TO_START': 'QLabel {color: orange ; font: bold}',
            'READY_TO_RESTORE': 'QLabel {color: orange ; font: bold}',

            'default': 'QLabel {color: black ; font: normal}',
        }

        self.incubators_count = None

        self._setup_ui_signals()
        self.show()

    def start_stop_autoupdate(self):
        """
        Start and stop the timer for automatic update status
        """
        checked = self.ui.timerGetStatus.isChecked()
        if checked:
            self.timer.start()
        else:
            self.timer.stop()

        self.logger.info("Automatic Get Status update " + ("enabled" if checked else "disabled"))

    def sendSshFsClose(self):
        """
        Unmounts the remote logs folder
        """
        instruction = u'fusermount -u {}'.format(self._localsshFS)
        subprocess.Popen(instruction, shell=True)

        # Reset table rows
        for x in xrange(self.logsTable.rowCount()):
            self.logsTable.removeRow(0)
        self.ui.contentsTab.setTabEnabled(3, False)

        msg = "Remote Logs folder unmounted"
        self.ui.statusbar.showMessage(msg)
        self.logger.info(msg)

    def sendSshFsOpen(self):
        # Function: mount of the remote logs folder

        if not os.path.ismount(self._localsshFS):
            instruction = u'echo {0} | sshfs {1}:{2} {3} -o password_stdin'.format(
                self.connection_data[3], self.connection_data[2], self._remotesshFS, self._localsshFS)
            self.sshfsOpenWin = subprocess.Popen(instruction, shell=True)
            self.ui.contentsTab.setTabEnabled(3, True)
        else:
            instruction = u'fusermount -u {}'.format(self._localsshFS)
            subprocess.Popen(instruction, shell=True)
            instruction = u'echo {0} | sshfs {1}:{2} {3} -o password_stdin'.format(
                self.connection_data[3], self.connection_data[2], self._remotesshFS, self._localsshFS)
            self.sshfsOpenWin = subprocess.Popen(instruction, shell=True)
            self.ui.contentsTab.setTabEnabled(3, True)

        self.ui.statusbar.showMessage("Remote Logs folder mounted")
        self.logger.info('Remote logs folder mounted on {}'.format(self.connection_data[0]))

    def sendSshTerminalOpen(self):
        # Function: Open a new terminal on remote machine

        instruction = u'gnome-terminal -e "sshpass -p {0} ssh {1}"'.format(
            self.connection_data[3], self.connection_data[2])
        subprocess.Popen(instruction, shell=True)
        self.ui.statusbar.showMessage("Terminal on WaspLab server opened")
        self.logger.info(
            'SSH Terminal open on {}'.format(
                self.connection_data[0]))

    def sendConnectionClose(self):
        # TODO: wat?
        print "ssh terminal closed"

    def sendConnectionCommand(self, memData):
        # Function: initialization of the SSH tunnel and port forwarding by
        # selected item on the connections Menu
        if len(self.connection_data) == 0:
            self.sshOpenWin = subprocess.Popen(str(self.connections[memData][1]), shell=True)
            self.connection_data = self.connections[memData]

            for i in xrange(self.ui.contentsTab.count()):
                self.ui.contentsTab.setTabEnabled(i, True)

            self.setWindowTitle(u'WaspLab Support Interface - {}'.format(self.connections[memData][0]))
            self.ui.statusbar.showMessage(u'Connected to {}'.format(self.connections[memData][0]))
            self.logger.info('SSH connection established on {}, '
                             'Tunneling activated'.format(self.connection_data[0]))
        else:
            QtGui.QMessageBox.warning(
                self,
                'Message',
                'ATTENTION: detected an opened connection.\n'
                'Please close all the terminal windows by typing "exit" and retry.')
            self.logger.warning(
                'SSH connection not activated on {} - {} connection still opened'.format(
                    self.connections[memData][0], self.connection_data[0]))
            self.connection_data = []

    def _check_password(self):
        """
        Shows a dialog asking for the password.
        Returns True if the user entered the administration password, False otherwise.
        """
        msg = u"Enter the password to connect Rpyc.\n" \
              u"ATTENTION: Very dangerous operation!"
        text, ok = QtGui.QInputDialog.getText(
            self, 'Input Dialog', msg, mode=QtGui.QLineEdit.Password)

        # Hashed password against which to check the input
        # TODO: this does not belong in the source
        hashed = '$2b$12$cQYDs7N6xI0WA2jDik.gbOcgLyJSdM6hi5a1jxRM5kqCo4ETPt4zC'

        return ok and (bcrypt.hashpw(str(text), hashed) == hashed)

    # TODO: this would be better as a context manager
    def rpyc_connection(self):
        """
        Initializes the rpyc connection between the local pc and the wasplab server.
        """
        if self._check_password():
            self.logger.info('Rpyc Connection: inserted correct password')
            if not self.rpyc_connected:
                self.rpyc = rpyc_client.rpyc_client(
                    CTomToolMainWindow.rpyc_host, CTomToolMainWindow.rpyc_port, self.incubators_count)
                self.rpyc_connected = True
            self.setFeatureButton.setEnabled(True)
            self.logger.info('Rpyc connection established')
            return True
        else:
            QtGui.QMessageBox.warning(
                self, 'Message', 'ATTENTION: Wrong password. Connection aborted.')
            self.setFeatureButton.setEnabled(False)
            self.logger.info(
                'Rpyc connection not established - Inserted wrong password')
            return False

    def rpyc_init_service(self):
        # Function: Definition of Features and GUI objects

        if self.rpyc_connection():
            self.groupFeature.addItems(self.rpyc.rpyc_get_group())
            self.listFeature.addItems(
                self.rpyc.rpyc_set_features_list('gate1'))
            self.logger.info('Rpyc features loaded')

    def on_groupfeature_changed(self, index):
        """
        Update Features group and list
        """
        self.listFeature.clear()
        self.listFeature.addItems(self.rpyc.rpyc_set_features_list(str(index)))

    def rpyc_feature_set_value(self, name, value):
        # Function: set new value of Feature by the name sent as parameter.
        # Check: it is used to activate or not the control of the READD ONLY
        # property of a feature
        feat = self.rpyc.rpyc_get_current_feature()

        if isinstance(self.rpyc.rpyc_get(feat['name']), int):
            res = self.rpyc.rpyc_set(int(value))
            if res:
                self.logger.info(
                    'Set {} with value {} as <type: int>'.format(
                        name, int(value)))
                return u"Set {} with value {} as <type: int>".format(
                    name, int(value))

            else:
                self.logger.error(
                    'Error to set {}  with value {} as <type: int>'.format(
                        name, int(value)))
                return u"Error to send the new value of {}".format(name)

        if isinstance(self.rpyc.rpyc_get(feat['name']), str):
            res = self.rpyc.rpyc_set(str(value))
            if res:
                self.logger.info(
                    'Set {} with value {} as <type: str>'.format(
                        name, int(value)))
                return u"Set {} with value {} as <type: str>".format(
                    name, str(value))

            else:
                self.logger.error(
                    'Error to set {}  with value {} as <type: str>'.format(
                        name, int(value)))
                return u"Error to send the new value of {}".format(name)

    def set_feature_value(self):
        # Function: update value on the GUI by the one written by the user
        new_value = self.newValueFeatureEdit.text()
        feat = self.rpyc.rpyc_get_current_feature()
        self.ui.resFeature.setText(
            self.rpyc_feature_set_value(
                feat['name'], new_value))
        time.sleep(1)
        feat = self.rpyc.rpyc_set_current_feature(
            str(self.groupFeature.currentText()), int(self.listFeature.currentIndex()))
        self.ui.valueFeature.setText(u"{} ({})".format(
            str(self.rpyc.rpyc_get(feat['name'])), type(self.rpyc.rpyc_get(feat['name']))))
        self.logger.info(
            'Updated {} with value {}'.format(
                feat['name'], new_value))

    def on_listfeature_changed(self, index):
        """
        Update values on the GUI by the feature selected by the user
        """
        feat = self.rpyc.rpyc_set_current_feature(
            str(self.groupFeature.currentText()), int(self.listFeature.currentIndex()))

        self.ui.nameFeature.setText(str(feat['name']))
        self.ui.addressFeature.setText(str(feat['addresses']))
        self.ui.descrFeature.setText(str(feat['description']))
        self.ui.valueFeature.setText(u"{} ({})".format(
            str(self.rpyc.rpyc_get(feat['name'])),
            type(self.rpyc.rpyc_get(feat['name'])))
        )
        self.ui.readonlyFeature.setText(str(feat['readonly']))
        self.ui.activeFeature.setText(str(feat['active']))
        self.logger.info('Selected {} in group {} by menus'.format(
                feat['name'],
                self.groupFeature.currentText()))

    def search_feature_inList(self):
        # Function: search and update Feature values on the GUI by the one
        # written by the user in SEARCH field

        #print (self.nameFeatureEdit.text())
        self.ui.nameFeature.setText(str('none'))
        self.ui.addressFeature.setText(str('none'))
        self.ui.descrFeature.setText(str('none'))
        self.ui.valueFeature.setText(str('none'))
        self.ui.readonlyFeature.setText(str('none'))
        self.ui.activeFeature.setText(str('none'))
        index_group = 0
        self.groupFeature.setCurrentIndex(index_group)
        self.listFeature.clear()
        self.listFeature.addItems(self.rpyc.rpyc_set_features_list('gate1'))

        [feat, key1, key2] = self.rpyc.rpyc_set_current_feature_by_search(
            self.nameFeatureEdit.text())
        self.groupFeature.setCurrentIndex(key1)
        self.listFeature.setCurrentIndex(key2)

        self.ui.nameFeature.setText(str(feat['name']))
        self.ui.addressFeature.setText(str(feat['addresses']))
        self.ui.descrFeature.setText(str(feat['description']))
        self.ui.valueFeature.setText(u"{} ({})".format(
            str(self.rpyc.rpyc_get(feat['name'])), type(self.rpyc.rpyc_get(feat['name']))))
        self.ui.readonlyFeature.setText(str(feat['readonly']))
        self.ui.activeFeature.setText(str(feat['active']))
        self.logger.info(
            'Selected {} in group {} by direct serch'.format(
                feat['name'],
                self.groupFeature.currentText()))

    def convert_plate_position(self, pos, subpos):
        """
        Converts the numeric position stored in the server (incubator.number)
        to the alphanumeric (letter + number) format used on the carousels' labels.
        """
        col_n = "ABCDEFGHIJKLMN"

        if pos in (1, 2, 3):
            row = (subpos / 14) + 1
            col = col_n[subpos % 14]
            position = u"Incubator {} - {}{} ".format(str(pos), str(col), str(row))
            self.logger.info('Position converted from {}.{} to {}'.format(pos, subpos, position))
            return position

        elif pos == 200:
            self.logger.info("Plate position: 200")
            return "End of Loading Line (200) - Barcode not readable or already present in the system"

        elif pos == 100:
            self.logger.info('Plate position: 100')
            return "Trash (100)"

        else:
            self.logger.info('Plate position: {}'.format(pos))
            return u"stacker {}".format(str(pos))

    def _req_user_password(self):
        """
        Gets the passwords of the webapp users.
        """
        self.logger.info('WaspLab users requested')

        with closing(ActivitiClient()) as activiti_db:
            result = activiti_db.send_query_user()

        msg = "Username\t\tPassword\n\n"
        for row in result:
            user = "{}\t\t{}\n".format(row[0], row[5])
            msg = msg + user
        QtGui.QMessageBox.information(self, 'WaspLab Users', msg)

    def _close_one_media(self):
        """
        Close a single media from the WaspLab
        """
        if self.ui.plateActiveValue.text() == 'True':

            if self._check_password():
                msg = u"You are going to close the plate {}, " \
                      u"deleting it from the interface and the database.\n\n" \
                      u"Are you really sure to perform this operation?".format(str(self.plateBrValue.text()))
                self.logger.info('Close media password correct and media active check passed.')
                reply = QtGui.QMessageBox.question(
                    self, 'Message', msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                if reply == QtGui.QMessageBox.Yes:
                    # TODO: check this result
                    result = self.proxy.closeMedia(str(self.plateBrValue.text()))
                    QtGui.QMessageBox.warning(self, 'Message', 'Plate closed.')
                    self.logger.info('Media {} closed.'.format(str(self.plateBrValue.text())))
                    time.sleep(1)
                    self._search_media()

            else:
                self.ui.statusbar.showMessage(u'Wrong password - Operation denied')
                QtGui.QMessageBox.warning(
                    self, 'Message', 'ATTENTION\nWrong password! Contact Technical Support')
                self.logger.warning('Inserted wrong Password in close media.')
        else:
            self.ui.statusbar.showMessage(u'Media already closed - Operation denied')
            QtGui.QMessageBox.warning(
                self, 'Message', 'ATTENTION\nThe media is already closed. Operation denied')
            self.logger.warning(
                'Media active check NOT passed. Media already closed.')

    def _select_barcodes_file_list(self):
        """
        Prompts the user to select the file that contains the list of barcodes to close,
        then reads the list of barcodes and stores it in self.barcodestoClose
        """
        fn = QtGui.QFileDialog.getOpenFileName(
            None,
            str("Select File of Barcode List of media to close"),
            QtCore.QDir.currentPath(),
            "All files (*.*)")

        if not fn:  # no file selected, abort
            return

        self.ui.closeListMediaEdit.setText(str(fn))

        # TODO: this should be a return value instead of an attribute
        self.barcodestoClose = []
        with open(fn, 'r') as f:
            for line in filter(None, map(str.strip, f)):
                if line.startswith("#"):
                    continue
                else:
                    self.barcodestoClose.append(line)

        self.closeListMediaButton.setEnabled(True)
        self.logger.info('Loaded Barcode list file: {}'.format(str(fn)))

    def _close_media_close_list(self):
        """
        Close a list of barcodes imported from file
        """
        # TODO: the file should be imported in this function
        if self._check_password():
            self.logger.info('Close list of media password correct')
            msg = u"You are going to close the media listed in the file, " \
                  u"deleting them from the interface and the database.\n" \
                  u"The amount of plates is {}.\n\n" \
                  u"Are you really sure to perform this operation?".format(len(self.barcodestoClose))
            reply = QtGui.QMessageBox.question(
                self, 'Message', msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                for barcode in self.barcodestoClose:
                    # TODO: check this result
                    result = self.proxy.closeMedia(barcode)
                    self.logger.info('Media {} closed.'.format(str(barcode)))
                QtGui.QMessageBox.warning(
                    self,
                    'Message',
                    'All the media are being closed. This operation will take several seconds. '
                    'Wait to restart the system until the counter on the PanelPC reads 0.')
        else:
            self.logger.warning('Inserted wrong Password in close list of media.')

    def _search_media(self):
        """
        Finds a media given the barcode in the closeMediaEdit line edit.
        """
        # TODO: the barcode should be a parameter
        barcode = str(self.ui.closeMediaEdit.text())
        media_info = self._query_media_by_barcode(barcode)

        if media_info:
            self.ui.plateBrValue.setText(str(media_info[6]))
            self.ui.plateStatusValue.setText(str(media_info[10]))
            self.ui.platePositionValue.setText(self.convert_plate_position(media_info[8], media_info[9]))
            self.ui.plateActiveValue.setText(str(media_info[4]))
            self.ui.closeMediaCloseButton.setEnabled(True)
            self.logger.info('Media {} info updated.'.format(str(barcode)))
        else:
            # TODO: set all the labels to none or something
            self.logger.warning('Media not found.')

    def _query_media_by_barcode(self, barcode):
        """
        Queries the database for a single plate by barcode.
        """
        with closing(Test3Client()) as test3_db:
            result = test3_db.send_query_mediaInfo(str(barcode))

        return result

    def _query_incubated_media(self, mode=0):
        """
        Queries all the active plates that are incubated.
        """
        with closing(Test3Client()) as test3_db:
            barcodes = test3_db.send_query_activeIncubated(int(mode))
        self.logger.info('Media query done with mode {}.'.format(mode))
        return barcodes

    def _close_media(self, mode):
        """
        Closes all the media in the given component.
        If the component is 0, it closes ALL the media in all the incubators.
        """
        if self._check_password():
            self.logger.info('Close media in incs password correct')

            barcodes = self._query_incubated_media(mode)

            if not self.rpyc_connected:
                self.rpyc = rpyc_client.rpyc_client(
                    CTomToolMainWindow.rpyc_host, CTomToolMainWindow.rpyc_port, self.incubators_count)
                self.rpyc_connected = True
                self.logger.info(
                    "Rpyc connection established for freeing incs in close media procedure")

            if mode == 0:
                msg = u"You are going to close all the media inside WaspLab, " \
                      u"deleting them by the interface and the database.\n" \
                      u"The amount of plates is {}.\n\n" \
                      u"Are you really sure to perform this operation?".format(len(barcodes))
            elif mode in (1, 2, 3):
                msg = u"You are going to close the plates media from INCUBATOR {}, " \
                      u"deleting them by the interface and the database.\n" \
                      u"The amount of plates is {}.\n\n" \
                      u"Are you really sure to perform this operation?".format(mode, len(barcodes))

            # Select the incubators to close the media
            incubators = [1, 2, 3] if mode == 0 else [mode]

            reply = QtGui.QMessageBox.question(
                self, 'Message', msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                for barcode in barcodes:
                    # Close all the selected media
                    # TODO: check this result
                    result = self.proxy.closeMedia(barcode)
                    self.logger.info('Closed media {}'.format(barcode))

                self.logger.info('Resetting PLC memory mode {}'.format(mode))
                for i in incubators:
                    self.rpyc.rpyc_set_direct('WL_FEAT_INC_{}_RESET_PLC_PLATES_MEMORY'.format(i), 1)

                time.sleep(1)

                for i in incubators:
                    self.rpyc.rpyc_set_direct('WL_FEAT_INC_{}_RESET_PLC_PLATES_MEMORY'.format(i), 0)
                self.logger.info('Freed the PLC memory mode {}'.format(mode))

                QtGui.QMessageBox.warning(
                    self,
                    'Message',
                    'All the media are being closed. This operation will take several seconds. '
                    'Wait to restart the system until the counter on the PanelPC reads 0.')

        else:
            self.ui.statusbar.showMessage(u'Wrong password - Connection denied')
            QtGui.QMessageBox.warning(
                self, 'Message', 'ATTENTION\nWrong password! Contact Technical Support')
            self.logger.warning('Inserted wrong password')

    def _generate_connections_menu(self):
        """
        Parses the connections configuration file and creates
        the corresponding menu actions.
        """
        self.connections = self._load_connections_file()
        self.connectionsMapping = QtCore.QSignalMapper(self)

        for index, (name, path, ssh_url, pwd, pwd_con) in enumerate(self.connections):
            item = self.ui.menuConnections.addAction(name)
            self.connectionsMapping.setMapping(item, index)
            item.triggered.connect(self.connectionsMapping.map)

        self.connectionsMapping.mapped.connect(self.sendConnectionCommand)
        self.logger.info('Connection Menu generated')

    def _load_connections_file(self):
        """
        Parses the connection info file.
        Returns a list of lists:
            [ [name, script, ssh_url, ssh_pwd, pwd_con] ]
        """
        connections_ini = ConfigParser.ConfigParser()
        connections_ini.read(self._connections)

        connections = []
        for name in connections_ini.sections():

            script = connections_ini.get(name, 'script')
            script = os.path.join(self._connectionsdir, script)
            if script.endswith('expect'):
                script = "gnome-terminal -e '{}'".format(script)

            ssh_url = connections_ini.get(name, 'ssh_url')
            ssh_pwd = connections_ini.get(name, 'ssh_pwd')
            pwd_con = connections_ini.get(name, 'pwd_con')

            # TODO: dicts are a pretty cool type
            params = [name, script, ssh_url, ssh_pwd, pwd_con]
            connections.append(params)

        return connections

    def _setup_ui_signals(self):
        """
        Connects the various signals and disables the controls that are not available
        before connection.
        """
        self.logger.info('Interface initialization')

        # region Disable all the tabs (they are enabled after connecting)
        for i in xrange(self.ui.contentsTab.count()):
            self.ui.contentsTab.setTabEnabled(i, False)

        for i in xrange(self.ui.commandsTab.count()):
            self.ui.commandsTab.setTabEnabled(i, False)
        # endregion

        # region Main window buttons
        self.ui.getStatusButton.clicked.connect(self.update_status)
        self.ui.timerGetStatus.stateChanged.connect(self.start_stop_autoupdate)
        self.ui.resetAlarmsButton.clicked.connect(self.send_resetAlarms_command)
        self.ui.getMsccsButton.clicked.connect(self._get_missing_starting_conditions)
        self.ui.searchButton.clicked.connect(self.on_searchbutton_clicked)
        # endregion

        # region Menu actions
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionOpen_Terminal.triggered.connect(self.sendSshTerminalOpen)
        self.ui.actionWL_Users.triggered.connect(self._req_user_password)
        self.ui.actionMount_logs_folder.triggered.connect(self.sendSshFsOpen)
        self.ui.actionUnmount_logs_folder.triggered.connect(self.sendSshFsClose)
        # endregion

        # region Features tab signals
        self.ui.groupFeature.currentIndexChanged[str].connect(self.on_groupfeature_changed)
        self.ui.listFeature.currentIndexChanged[str].connect(self.on_listfeature_changed)
        self.ui.connectRpycButton.clicked.connect(self.rpyc_init_service)
        self.ui.setFeatureButton.clicked.connect(self.set_feature_value)
        self.ui.featureButton.clicked.connect(self.search_feature_inList)
        # endregion

        # region Close media tab
        self.ui.closeAllMediaSys.clicked.connect(lambda: self._close_media(0))
        self.ui.closeAllMediaInc1.clicked.connect(lambda: self._close_media(1))
        self.ui.closeAllMediaInc2.clicked.connect(lambda: self._close_media(2))
        self.ui.closeAllMediaInc3.clicked.connect(lambda: self._close_media(3))
        self.ui.closeMediaSearchButton.clicked.connect(self._search_media)
        self.ui.closeMediaCloseButton.clicked.connect(self._close_one_media)
        self.ui.closeListMediaButton.clicked.connect(self._close_media_close_list)
        self.ui.closeListMediaSelectButton.clicked.connect(self._select_barcodes_file_list)
        # endregion

        # region Unloading Queue tab
        # Queue update buttons
        self.ui.unloadQueueButtonInc1.clicked.connect(lambda: self._get_incubator_unloading_queue(1))
        self.ui.unloadQueueButtonInc2.clicked.connect(lambda: self._get_incubator_unloading_queue(2))
        self.ui.unloadQueueButtonInc3.clicked.connect(lambda: self._get_incubator_unloading_queue(3))
        self.ui.unloadQueueButtonInc1.setEnabled(False)
        self.ui.unloadQueueButtonInc2.setEnabled(False)
        self.ui.unloadQueueButtonInc3.setEnabled(False)
        # Export Selection buttons
        self.ui.exportQueueButtonInc1.clicked.connect(lambda: self._export_incubator_queue(1))
        self.ui.exportQueueButtonInc2.clicked.connect(lambda: self._export_incubator_queue(2))
        self.ui.exportQueueButtonInc3.clicked.connect(lambda: self._export_incubator_queue(3))
        self.ui.exportQueueButtonInc1.setEnabled(False)
        self.ui.exportQueueButtonInc2.setEnabled(False)
        self.ui.exportQueueButtonInc3.setEnabled(False)
        # endregion

        # region Buttons to enable / disable the incubators
        self.ui.activeInc1Button.clicked.connect(lambda: self._activate_incubator(1))
        self.ui.activeInc2Button.clicked.connect(lambda: self._activate_incubator(2))
        self.ui.activeInc3Button.clicked.connect(lambda: self._activate_incubator(3))
        self.ui.deactiveInc1Button.clicked.connect(lambda: self._deactivate_incubator(1))
        self.ui.deactiveInc2Button.clicked.connect(lambda: self._deactivate_incubator(2))
        self.ui.deactiveInc3Button.clicked.connect(lambda: self._deactivate_incubator(3))
        self.ui.activeInc1Button.setEnabled(False)
        self.ui.activeInc2Button.setEnabled(False)
        self.ui.activeInc3Button.setEnabled(False)
        self.ui.deactiveInc1Button.setEnabled(False)
        self.ui.deactiveInc2Button.setEnabled(False)
        self.ui.deactiveInc3Button.setEnabled(False)
        # endregion

        # region Start, stop and restore buttons

        # Start buttons
        self.ui.startButtonLine.clicked.connect(lambda: self._start_stop_restore_component('start', 0))
        self.ui.startButtonInc1.clicked.connect(lambda: self._start_stop_restore_component('start', 1))
        self.ui.startButtonInc2.clicked.connect(lambda: self._start_stop_restore_component('start', 2))
        self.ui.startButtonInc3.clicked.connect(lambda: self._start_stop_restore_component('start', 3))
        self.ui.startButtonLine.setEnabled(False)
        self.ui.startButtonInc1.setEnabled(False)
        self.ui.startButtonInc2.setEnabled(False)
        self.ui.startButtonInc3.setEnabled(False)

        # Stop buttons
        self.ui.stopButtonLine.clicked.connect(lambda: self._start_stop_restore_component('stop', 0))
        self.ui.stopButtonInc1.clicked.connect(lambda: self._start_stop_restore_component('stop', 1))
        self.ui.stopButtonInc2.clicked.connect(lambda: self._start_stop_restore_component('stop', 2))
        self.ui.stopButtonInc3.clicked.connect(lambda: self._start_stop_restore_component('stop', 3))
        self.ui.stopButtonLine.setEnabled(False)
        self.ui.stopButtonInc1.setEnabled(False)
        self.ui.stopButtonInc2.setEnabled(False)
        self.ui.stopButtonInc3.setEnabled(False)

        # Restore buttons
        self.ui.restoreButtonLine.clicked.connect(lambda: self._start_stop_restore_component('restore', 0))
        self.ui.restoreButtonInc1.clicked.connect(lambda: self._start_stop_restore_component('restore', 1))
        self.ui.restoreButtonInc2.clicked.connect(lambda: self._start_stop_restore_component('restore', 2))
        self.ui.restoreButtonInc3.clicked.connect(lambda: self._start_stop_restore_component('restore', 3))
        self.ui.restoreButtonLine.setEnabled(False)
        self.ui.restoreButtonInc1.setEnabled(False)
        self.ui.restoreButtonInc2.setEnabled(False)
        self.ui.restoreButtonInc3.setEnabled(False)

        # endregion Start, stop and restore buttons

        # region Software services buttons
        self.ui.stopButtonSwSer.clicked.connect(self.send_stopSwSer_command)
        self.ui.startButtonSwSer.clicked.connect(self.send_startSwSer_command)
        self.ui.statusButtonSwSer.clicked.connect(self.send_statusSwSer_command)
        # endregion

        # region Close media buttons
        self.ui.closeMediaButtonInc1.clicked.connect(lambda: self._close_first_media_in_incubator(1))
        self.ui.closeMediaButtonInc2.clicked.connect(lambda: self._close_first_media_in_incubator(2))
        self.ui.closeMediaButtonInc3.clicked.connect(lambda: self._close_first_media_in_incubator(3))
        self.ui.closeMediaButtonInc1.setEnabled(False)
        self.ui.closeMediaButtonInc2.setEnabled(False)
        self.ui.closeMediaButtonInc3.setEnabled(False)
        # endregion

        self._generate_connections_menu()

        self.ui.statusbar.showMessage(
            'Interface initialized - Select from CONNECTIONS menu the WaspLab to connect')

    def _close_first_media_in_incubator(self, inc_num):
        """
        Close the first media in the unloading queue of the given incubator.
        """
        queue = self.proxy.getUnloadingQueue(str(inc_num))
        barcode = queue[0][1]  # TODO: what if the queue is empty?

        quit_msg = u"Are you sure to CLOSE the media " + barcode + " from incubator {}?".format(inc_num)
        reply = QtGui.QMessageBox.question(
            self,
            'Message',
            quit_msg,
            QtGui.QMessageBox.Yes,
            QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            result = self.proxy.closeMedia(barcode)
            if result:
                self.logger.info(
                    'Removed media {} from the unloading queue '
                    'of Incubator {}. Media closed'.format(barcode, inc_num))
                info_msg = "Closed media " + barcode
                QtGui.QMessageBox.information(self, 'Message', info_msg)
                self.ui.statusbar.showMessage(info_msg)
            else:
                QtGui.QMessageBox.warning(
                    self,
                    'Message',
                    'ERROR: media not present in the unloading queue of incubator {}'.format(inc_num))
                self.logger.warning(
                    'Media {} not present in the unloading queue of incubator {}'.format(barcode, inc_num))

    def update_status(self):
        """
        Updates the status of the WaspLab and updates the GUI to match.
        """
        self.logger.info('Status update requested')

        # region Disable the buttons, reset the labels
        self.ui.statusLine.setText("Not Present")
        self.ui.statusInc1.setText("Not Present")
        self.ui.statusInc2.setText("Not Present")
        self.ui.statusInc3.setText("Not Present")

        self.ui.numPlateInc1.setText("---")
        self.ui.numPlateInc2.setText("---")
        self.ui.numPlateInc3.setText("---")

        self.ui.unloadQueueButtonInc1.setEnabled(False)
        self.ui.unloadQueueButtonInc2.setEnabled(False)
        self.ui.unloadQueueButtonInc3.setEnabled(False)

        self.ui.exportQueueButtonInc1.setEnabled(False)
        self.ui.exportQueueButtonInc2.setEnabled(False)
        self.ui.exportQueueButtonInc3.setEnabled(False)

        self.ui.closeMediaButtonInc1.setEnabled(False)
        self.ui.closeMediaButtonInc2.setEnabled(False)
        self.ui.closeMediaButtonInc3.setEnabled(False)

        self.ui.statusLine.setStyleSheet(self.palette['default'])
        self.ui.statusInc1.setStyleSheet(self.palette['default'])
        self.ui.statusInc2.setStyleSheet(self.palette['default'])
        self.ui.statusInc3.setStyleSheet(self.palette['default'])

        self.ui.actionClose_ALL_medias.setEnabled(False)
        self.ui.actionClose_media_in_INC1.setEnabled(False)
        self.ui.actionClose_media_in_INC2.setEnabled(False)
        self.ui.actionClose_media_in_INC3.setEnabled(False)
        # endregion

        # Update status information
        info = self._get_system_info()
        status = self._get_system_status()

        # Update Alarms Table
        self._update_alarms_table(self.ui.alarms, self.proxy.getAlarms())

        self.incubators_count = len(status) - 1
        if self.incubators_count > 0:
            self.ui.contentsTab.setTabEnabled(5, True)

        # region Update the labels and the buttons status for every component
        for index, status_value, element_active in status:

            if index == '4':  # SW services
                self.ui.commandsTab.setTabEnabled(4, True)
                # TODO: isn't this basically always enabled regardless of the components' status?
                # Nothing else to do for these
                continue
            
            if index == '0':
                # For the line, just get the label to update
                status_label = self.ui.statusLine

            elif index in ('1', '2', '3'):
                # For the incubators, also enable / disable the corresponding buttons
                self.ui.actionClose_ALL_medias.setEnabled(True)
                status_label = getattr(self.ui, 'statusInc' + index)
                getattr(self.ui, 'unloadQueueButtonInc' + index).setEnabled(True)
                getattr(self.ui, 'exportQueueButtonInc' + index).setEnabled(True)

                if status_value == "EMERGENCY":
                    getattr(self.ui, 'closeMediaButtonInc' + index).setEnabled(True)
                    getattr(self.ui, 'actionClose_media_in_INC' + index).setEnabled(True)
                    getattr(self.ui, 'deactiveInc{}Button'.format(index)).setEnabled(True)
                    getattr(self.ui, 'activeInc{}Button'.format(index)).setEnabled(False)

                if status_value == "Not Enabled":
                    getattr(self.ui, 'activeInc{}Button'.format(index)).setEnabled(True)
                    getattr(self.ui, 'deactiveInc{}Button'.format(index)).setEnabled(False)

            else:
                raise RuntimeError("Unexpected index found when updating the status: {!r}".format(index))

            # region Update the status label and the corresponding commands tab
            index = int(index)
            self.ui.commandsTab.setTabEnabled(index, True)
            self._set_commands_status(status_value, index)

            # If there's an alarm on the component switch to alarm regardless of the actual status.
            if self.alarmStatus[index]:
                status_value = 'ALARM'

            status_label.setText(status_value)
            status_label.setStyleSheet(self.palette.get(status_value) or self.palette['default'])
            # endregion

        # endregion Update the labels and the buttons status for every component

        # Update of the number of plates
        for index, incType, numPlate, capPlate in info:
            if index in ('1', '2', '3'):
                getattr(self.ui, 'numPlateInc' + index).setText(str(numPlate) + '/' + str(capPlate))

    def _set_commands_status(self, status, index):
        """
        Enables or disables the start, stop and restore buttons
        for the component with the given index according to its status.
        """
        index = str(index)
        if index == '0':
            stop_button = self.ui.stopButtonLine
            start_button = self.ui.startButtonLine
            restore_button = self.ui.restoreButtonLine
        else:
            stop_button = getattr(self.ui, 'stopButtonInc' + index)
            start_button = getattr(self.ui, 'startButtonInc' + index)
            restore_button = getattr(self.ui, 'restoreButtonInc' + index)

        for btn in (start_button, stop_button, restore_button):
            btn.setEnabled(False)

        if status == "IN_CYCLE" and not self.alarmStatus[0]:
            stop_button.setEnabled(True)
        elif status == "READY_TO_START":
            start_button.setEnabled(True)
        elif status == "READY_TO_RESTORE":
            restore_button.setEnabled(True)
        else:
            # all stay disabled
            pass

        timing = datetime.datetime.now().time().isoformat()
        self.ui.statusbar.showMessage("Status updated at {}".format(timing[:-7]))

    def _get_system_status(self):
        """
        Get Status of the elements saved in a list of lists:
            [['0', [alarms...]],['1', [alarms...]], ...]
        where  '0' = line, '1' = inc1 and etc.
        """
        line_status = self.proxy.getLineStatus()
        incs_status = self.proxy.getIncubatorsStatus()

        status = [['0', line_status[0], True]]

        with closing(Test3Client()) as test3_db:
            inc_actives = test3_db.send_query_statusInc()

        for item in inc_actives:
            tmp_status = incs_status[str(item[0])][0] if item[1] is True else 'Not Enabled'
            status.append([str(item[0]), tmp_status, item[1]])

        status.append(['4', 'Active', True])  # Sw services

        self.logger.info('System Status acquired')
        return status

    def _get_system_info(self):
        """
        Gets the amount of plates, type and capacity for the incubators.
        """
        info_incs = self.proxy.getIncubatorsInfo()
        info = []
        for key in info_incs:
            info.append([key, info_incs[key][1]['type'],
                         info_incs[key][0],
                         info_incs[key][1]['capacity']])
        self.logger.info('System Info acquired (type and capacity)')

        return info

    def _get_missing_starting_conditions(self):
        """
        Gets the missing starting conditions from the server
        and updates the list view.
        """
        msccs_list = self.proxy.getMsccs()
        self._populate_missing_conditions_table(
            self.ui.msccs,
            msccs_list,
            self.ui.elementMsccs.currentText())
        self.ui.statusbar.showMessage(
            u"Missing Sarting Condition table updated on {}".format(
                self.ui.elementMsccs.currentText()))
        self.logger.info(
            "Missing Sarting Condition updated on {}".format(
                self.ui.elementMsccs.currentText()))

    # region Incubators activation / deactivation
    def _is_incubator_active(self, inc):
        """
        Checks if the given incubator is active or not
        """
        status = self._get_system_status()
        return status[int(inc)][2]

    def _activate_incubator(self, inc_num):

        if self._is_incubator_active(str(inc_num)):
            QtGui.QMessageBox.warning(
                self, 'Message', 'ATTENTION\nIncubator {} already activated'.format(inc_num))
            return

        if self._check_password():
            msg = u"You are going to activate Incubator {}.\n" \
                  u"Are you really sure to perform this operation?".format(inc_num)
            reply = QtGui.QMessageBox.question(
                self, 'Message', msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                # TODO: check this result
                result = self.proxy.setIncubatorActive(inc_num, True)
                # print "Inc {} activated".format(inc_num)
                QtGui.QMessageBox.warning(
                    self, 'Message', 'Incubator {} Activated.'.format(inc_num))
                self.logger.info('Incubator {} activated.'.format(inc_num))
                time.sleep(1)
                self.update_status()
            else:
                pass

        else:
            self.ui.statusbar.showMessage(
                u'Wrong password - Operation denied')
            QtGui.QMessageBox.warning(
                self, 'Message', 'ATTENTION\nWrong password! Contact Technical Support')
            self.logger.warning('Inserted wrong Password.')

    def _deactivate_incubator(self, inc_num):
        """
        Disables an incubator. The incubator is bypassed and marked as inactive:
        it is effectively disconnected from the rest of the system.
        """
        if not self._is_incubator_active(str(inc_num)):
            QtGui.QMessageBox.warning(
                self, 'Message', 'ATTENTION\nIncubator {} already disabled'.format(inc_num))
            return

        if self._check_password():
            msg = u"You are going to disable Incubator {}.\n" \
                  u"Are you really sure to perform this operation?".format(inc_num)
            reply = QtGui.QMessageBox.question(
                self, 'Message', msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                # TODO: check this result
                result = self.proxy.setIncubatorActive(inc_num, False)
                QtGui.QMessageBox.warning(
                    self, 'Message', 'Incubator {} disabled.'.format(inc_num))
                self.logger.info('Incubator {} disabled.'.format(inc_num))
                time.sleep(1)
                self.update_status()

        else:
            self.ui.statusbar.showMessage(
                u'Wrong password - Operation denied')
            QtGui.QMessageBox.warning(
                self, 'Message', 'ATTENTION\nWrong password! Contact Technical Support')
            self.logger.warning('Inserted wrong Password.')
    # endregion

    def send_startSwSer_command(self):
        """Send (Re)Start command to software"""
        self.ui.statusbar.showMessage("Processing your request")
        [btncmd.setEnabled(False) for btncmd in [self.startButtonSwSer,
                                                 self.stopButtonSwSer]
         ]
        btn = self.selectButtonSwSer.checkedButton()
        if btn is None:
            msg = "No service has been selected"
        else:
            service = str(btn.text()).lower()
            action = "restart"
            retcode, out = self._send_command_to_service(service, action)

            if retcode == -1:
                msg = "Impossible to restart the service, see logs for details"
            else:
                msg = "Service has been (re)started"
        self.ui.statusbar.showMessage(msg)
        self.logger.info(msg)
        [btncmd.setEnabled(True) for btncmd in [self.startButtonSwSer,
                                                self.stopButtonSwSer]
         ]

    def send_stopSwSer_command(self):
        """Send Stop command to software"""
        self.ui.statusbar.showMessage("Processing your request")
        [btncmd.setEnabled(False) for btncmd in [self.startButtonSwSer,
                                                 self.stopButtonSwSer]
         ]
        btn = self.selectButtonSwSer.checkedButton()
        if btn is None:
            msg = "No service has been selected"
        else:
            service = str(btn.text()).lower()
            action = "stop"
            retcode, out = self._send_command_to_service(service, action)

            if retcode == -1:
                msg = "Impossible to stop the service, see logs for details"
            else:
                msg = "Service has been stopped"
        self.ui.statusbar.showMessage(msg)
        self.logger.info(msg)
        [btncmd.setEnabled(True) for btncmd in [self.startButtonSwSer,
                                                self.stopButtonSwSer]
         ]

    def send_statusSwSer_command(self):
        """Send Status command to software"""
        self.ui.statusbar.showMessage("Processing your request")
        btn = self.selectButtonSwSer.checkedButton()
        if btn is None:
            msg = "No service has been selected"
        else:
            service = str(btn.text()).lower()
            action = "status"
            retcode, out = self._send_command_to_service(service, action)

            if retcode == -1:
                msg = "Impossible to check the status of the service, see logs for details"
            else:
                msg = out
        self.ui.statusbar.showMessage(msg)
        self.logger.info(msg)

    def _send_command_to_service(self, service, action='status'):
        """
        Sends a command to the selected software service (wlag, scheduler, awluic...)
        """
        pwd = self.connection_data[3]
        host = self.connection_data[2]
        script = self._restartscript

        # scp copy the script to the remote machine
        cmd = u'sshpass -p {0} scp {1} {2}:.'.format(pwd, script, host)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        exit_code = "SUCCESS" if len(out) == 0 else "FAILURE"

        self.logger.info("running {0}, got {1}, interpreted as {2}".format(
            cmd, out, exit_code))

        if exit_code != "SUCCESS":
            return (-1, None)

        # execute the script on the remote machine
        basescript = os.path.basename(script)
        cmd = u'sshpass {4} ssh {0} "bash {1} {2} {3} {4}"'.format(
            host, basescript, service, action, pwd)

        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        exit_code, msg = out.split('\n', 1)

        if out is not None:
            out = out.replace('\n', ' ')

        self.logger.info("running {0}, got {1} {2}, interpreted as {3}".format(
            cmd, out, err, exit_code))

        # TODO: check this exit code
        if exit_code == "FAILURE":
            return (-1, None)

        return (0, out)

    def _start_stop_restore_component(self, action, comp_num):
        """
        Sends the start, stop, or restore command to the line or to an incubator
        """
        action = action.upper()
        if action not in ('START', 'STOP', 'RESTORE'):
            raise ValueError("Unsupported action")

        comp_name = "Incubator {}".format(comp_num) if comp_num > 0 else "the line"
        msg = u"Are you sure you want to {} {}?".format(action, comp_name)
        reply = QtGui.QMessageBox.question(
            self, 'Message', msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            command = getattr(self.proxy, "{}_command".format(action.lower()))
            command(comp_num)
            time.sleep(1)
            self.update_status()
            self.ui.statusbar.showMessage("{} sent to {}".format(action, comp_name))
            self.logger.info("{} sent to {}".format(action, comp_name))
        else:
            return

    def _get_incubator_unloading_queue(self, inc_num):
        """
        Gets the unloading queue for an incubator
        and updates the corresponding table view.
        """
        inc_num = str(inc_num)
        queue = self.proxy.getUnloadingQueue(inc_num)
        table = getattr(self.ui, 'unloadQueueInc' + inc_num)
        self._populate_unloading_queue_table(table, queue)
        self.ui.statusbar.showMessage("Updated the unloading queue of incubator {}".format(inc_num))
        self.logger.info("Updated the unloading queue of incubator {}".format(inc_num))

    def _save_list_to_file(self, output):
        """
        Prompts the user for a filename to save a list and writes each item
        to the selected file.
        """
        filename = QtGui.QFileDialog.getSaveFileName(None, 'Save File', '/')
        if not filename:
            return
        try:
            with open(filename, 'w') as fout:
                for item in output:
                    print >> fout, item
            self.logger.info("List has been saved on {0}".format(filename))
        except IOError as e:
            self.logger.info("File does not exist")
            self.logger.info(e)

    def _export_incubator_queue(self, inc_num):
        self.logger.info("Exporting incubator {}'s unload queue".format(inc_num))
        table = getattr(self.ui, 'unloadQueueInc' + str(inc_num))
        barcodes = self._export_barcodes(table)
        self._save_list_to_file(barcodes)

    def _export_barcodes(self, table):
        """
        Exports all the barcodes from an unloading queue table
        that have been selected for export.
        Returns the barcodes as a list of strings.
        """
        barcodes = []
        for rowno in xrange(table.rowCount()):
            item = table.item(rowno, 3)
            if item.isChecked():
                barcode = str(table.item(rowno, 1).text())
                self.logger.debug("adding barcode {0} to the queue".format(barcode))
                barcodes.append(barcode)

        return barcodes

    def send_resetAlarms_command(self):
        """
        Sends the reset alarms command to the line and all the incubators.
        """
        for i in xrange(self.incubators_count + 1):
            self.proxy.reset_alarm(i)

        self.ui.statusbar.showMessage("Reset Alarm sent")
        self.logger.info("Reset alarms command sent")

    def _populate_unloading_queue_table(self, queuetable, queue):
        """
        Update unloading queue table.
        Accepts element in format [[u'--', u'barcode', u'--'], ]
        """
        for x in xrange(queuetable.rowCount()):
            queuetable.removeRow(0)

        for queue_el in reversed(queue):
            queuetable.insertRow(0)
            (priority, barcode, destination) = queue_el

            item = QtGui.QTableWidgetItem(str(priority))
            queuetable.setItem(0, 0, item)

            item = QtGui.QTableWidgetItem(barcode)
            queuetable.setItem(0, 1, item)

            item = QtGui.QTableWidgetItem(str(destination))
            queuetable.setItem(0, 2, item)

            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable |
                          QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)
            queuetable.setItem(0, 3, item)

    def _update_alarms_table(self, alarmtable, alarms):
        """
        Updates the table view with the current alarms.
        alarms is a list of lists with the following format:
            [ [component, priority, address, description],
              [u'Line', 1, u'2000.08', u'ExampleAlarm'] ]
        """
        # Reset the component's status and remove all the rows from the table
        self.alarmStatus = [False, False, False, False]
        for x in xrange(alarmtable.rowCount()):
            alarmtable.removeRow(0)

        if not alarms:
            return False

        for alm in reversed(alarms):
            alarmtable.insertRow(0)
            item = QtGui.QTableWidgetItem(alm[0])
            alarmtable.setItem(0, 0, item)
            if alm[0] == "Line":
                self.alarmStatus[0] = True
            elif alm[0] == "Incubator 1":
                self.alarmStatus[1] = True
            elif alm[0] == "Incubator 2":
                self.alarmStatus[2] = True
            elif alm[0] == "Incubator 3":
                self.alarmStatus[3] = True

            item = QtGui.QTableWidgetItem(alm[2])
            alarmtable.setItem(0, 1, item)

            text_field = u"{}: {}".format(alm[3], alm[4]) if alm[4] else alm[3]
            item = QtGui.QTableWidgetItem(text_field)
            alarmtable.setItem(0, 2, item)

        return True

    def _populate_missing_conditions_table(self, mscctable, msccs, element):
        """
        Populates the missing starting conditions table .
        Accept msccs in format [[u'Line', 1, u'2000.08', u'ExampleMSSC'], ]
        """
        for x in xrange(mscctable.rowCount()):
            mscctable.removeRow(0)

        for mscc in reversed(msccs):
            if mscc[0] == element:
                mscctable.insertRow(0)
                item = QtGui.QTableWidgetItem(mscc[2])
                mscctable.setItem(0, 0, item)
                item = QtGui.QTableWidgetItem(mscc[3])
                mscctable.setItem(0, 1, item)

    def _check_filenames_search(self):
        # function: enable the searching on the logs selected
        filenames = []

        if self.ui.allLogsCombo.isChecked():
            filenames.append("all.log")
        if self.ui.wlagLogsCombo.isChecked():
            filenames.append("WLAG.log")

        return filenames

    def on_searchbutton_clicked(self):
        """
        Greps through the selected log files using the given regex.
        """
        filenames = self._check_filenames_search()
        regex = unicode(self.ui.searchEdit.text()).strip()
        if not regex or not filenames:
            return

        for x in xrange(self.ui.logsTable.rowCount()):
            self.ui.logsTable.removeRow(0)

        grin_args = [u"-n", u"-i"] + [regex]
        parser = grin.get_grin_arg_parser()
        try:
            args = parser.parse_args(grin_args)
        except SystemExit as e:
            # If somehow arguments are wrong the parser tries to exit the interpreter
            return
        else:
            args.use_color = False

        g = grin.GrepText(re.compile(regex), args)

        for filename in filenames:
            report = g.grep_a_file(u"{0}/{1}".format(self._localsshFS, filename))

            for line in report.split(u"\n"):
                line = unicode(line.strip())
                if len(line) == 0 or ":" not in line:
                    continue

                parts = filter(lambda item: len(item) > 0, line.split(u":"))
                if len(parts) > 1:
                    self.logsTable.insertRow(self.logsTable.rowCount())
                    item = QtGui.QTableWidgetItem(filename)
                    self.logsTable.setItem(self.logsTable.rowCount() - 1, 0, item)

                    text = line[(len(parts[0]) + 1):].strip()
                    item = QtGui.QTableWidgetItem(u"{0}".format(text))
                    self.logsTable.setItem(
                        self.logsTable.rowCount() - 1, 1, item)

        self.ui.statusbar.showMessage("Search completed")
        self.logger.info("Searched {} in logs".format(self.ui.searchEdit.text()))
