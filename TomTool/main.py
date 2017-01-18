#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging.config
from PyQt4 import QtGui

from TomTool.GUI.CTomToolMainWindow import CTomToolMainWindow

def main(args):

    if args.conf is None:
        # Default to the usual path if the argument is not given
        args.conf = os.path.join(os.path.expanduser('~'), '.TomTool', 'tomtool.ini')

    if not os.path.exists(args.conf):
        raise EnvironmentError("The configuration file {} does not exist".format(args.conf))

    logging.config.fileConfig(args.conf)

    app = QtGui.QApplication(sys.argv)
    ex = CTomToolMainWindow(args.conf)
    sys.exit(app.exec_())
