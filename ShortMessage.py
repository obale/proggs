#!/usr/bin/env python
import sys
from optparse import OptionParser
import dbus

"""
Implements the following functions:

    public sendSMS(phone_number, message)
    @param phone_number The telephone number of the receiver.
    @param message The message which should be send (can be longer then one
                   SMS)
"""
class ShortMessage:
    msglength = 140
    def __init__(self):
        pass

    def sendSMS(self, number, message):
        bus = self.getBus("org.freesmartphone.ogsmd",\
                "/org/freesmartphone/GSM/Device",\
                "org.freesmartphone.GSM.SMS")
        msglist = self._splitMessage(message)
        id = 1
        count = 1
        for entry in msglist:
            try:
                bus.SendMessage(number, entry, {"csm_id":id,"csm_num":len(msglist),"csm_seq":count})
            except:
                print "[!!] Unable to open SendMessage(...)! Maybe you are not on \
the mobile device."
            count += 1

    def readSMS(self, type):
        bus = self.getBus("org.freesmartphone.ogsmd",\
                "/org/freesmartphone/GSM/Device",\
                "org.freesmartphone.GSM.SIM")
        smsArray = bus.RetrieveMessagebook(type)
        for entry in smsArray:
            infos = entry[4]
            try:
                timestamp = infos['timestamp']
            except:
                timestamp = "No timestamp found"
            try:
                encoding = infos['alphabet']
            except:
                encoding = "No alphabet found"
            try:
                data = infos['data']
            except:
                data = "No data found"

            print "[" + str(entry[0]) + "] \033[1;32mSender   \033[m   : " + entry[2]
            print "[" + str(entry[0]) + "] \033[1;32mTimestamp\033[m   : " + timestamp
            print "[" + str(entry[0]) + "] \033[1;32mAlphabet \033[m   : " + encoding
            print "[" + str(entry[0]) + "] \033[1;32mMessage  \033[m   : " + entry[3].strip('\n')
            if encoding == "binary":
                print "[" + str(entry[0]) + "] \033[1;32mBinary Data is available.\033[m"
                fd = open('/tmp/binary_sms' + str(entry[0]), 'w')
                fd.write(data.tostring())
            print

    def getBus(self, dbusConnection, dbusObject, dbusInterface):
        try:
            bus = dbus.SystemBus()
            oMux = bus.get_object(dbusConnection, dbusObject)
            iMux = dbus.Interface(oMux, dbusInterface)
            return iMux
        except dbus.DBusException, e:
            print "[!!] Unable to connect to dbus: %s" %str(e)

    def _splitMessage(self, message):
        tmp = message
        msglist = []
        begin = 0
        while tmp:
            end = begin + self.msglength
            tmp = message[begin:end]
            if tmp: msglist.append(tmp)
            begin = end
        return msglist

"""
Start the main program.
"""
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-n", "--number", type="str", dest="number", help="The \
telephone number of the receiver.", metavar="PHONE_NUMBER")
    parser.add_option("-m", "--msg", type="str", dest="message", help="The \
message which should be send.")
    parser.add_option("-r", "--read", type="str", dest="type", help="Read \
the stored SMS. TYPE takes the following options: all, unread, read, sent, \
unsent")

    (options, args) = parser.parse_args()
    obj = ShortMessage()
    if options.number is not None and options.message is not None:
        obj.sendSMS(options.number, options.message)
    if options.type is not None:
        obj.readSMS(options.type)
    else:
        print "[!] Please specifiy a option. For more information see \
-h/--help"
        sys.exit(0)
