# -*- coding: UTF-8 -*-
import helper
import datetime

def init():
    if helper.getLogging():

        logfile = helper.getLogfile()
        file = open(logfile, 'a')
        dt = datetime.datetime.now()
        now = dt.strftime("%A, %d. %B %Y %H:%M")
        str = '======================== BEGIN LOGIN: ' + now \
+ ' ========================\n'
        file.write(str)
        file.close()


def logging(line):
    if not helper.getLogging():
        return
    logfile = helper.getLogfile()
    file = open(logfile, 'a')
    file.write(line + '\n')
    file.close

