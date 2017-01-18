import xmlrpclib


class xmlrpc_client():
    def __init__(self,address):
        self.px = xmlrpclib.ServerProxy(address)

    def getIncubatorsInfo(self):
        #Get incubators info (filling and type)
        info = self.px.get_incubators_info()
        return info

    def getAlarms(self):
        #Get alarms list
        alarmsList = self.px.get_active_alarms()
        return alarmsList

    def getLineStatus(self):
        #Get Line status
        line = self.px.get_line_status()
        return line

    def getIncubatorsStatus(self):
        #Get Incubators status
        incs = self.px.get_incubators_status()
        return incs

    def getUnloadingQueue(self,inc):
        #Get unloading queue on a specific incubator
        queues = self.px.get_incubators_unload_queue()
        return queues[inc]

    def closeMedia(self, barcodeMedia):
        #Send request to close media passed as parameter
        result = self.px.close_media(barcodeMedia)
        return result[0]

    def getMsccs(self):
        #Get missing starting condition
        msccs = self.px.get_missing_start_cycle_conditions()
        return msccs

    def start_command(self,mode):
        if mode==0:
            self.px.start_line()
        else:
            self.px.start_incubator(mode)

    def stop_command(self,mode):
        if mode==0:
            self.px.stop_line()
        else:
            self.px.stop_incubator(mode)

    def restore_command(self,mode):
        if mode==0:
            self.px.restore_line()
        else:
            self.px.restore_incubator(mode)

    def reset_alarm(self,mode):
        if mode==0:
            self.px.reset_line_alarms()
        else:
            self.px.reset_incubator_alarms(mode)

    def setIncubatorActive(self,inc, value):
        return self.px.set_incubator_active(inc,bool(value))

