#!/usr/bin/python
# -*- coding: UTF-8 -*-
# tweetC2 - A twitter bot, which handles commands and reacts on it. 
#           (C2 = command & control)
#
# (C) 2009 by MokSec Project
# Written by Alex Oberhauser <oberhauseralex@networld.to>
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>
import sys
import signal
import time
from modules import config
from modules import twitterApi
from modules import commandParser
from modules import commandHandler
from modules import helper

def checkCommand(signum, frame):
    seconds = 30
    handler = commandHandler.commandHandler()
    handler.handleCommand()
    msg = 'Sleeping for ' + str(seconds) + ' seconds'
    helper.printInfoVerbose(msg)
    signal.alarm(seconds)

def quit(signum, frame):
    helper.printInfoVerbose('Shutting down...')
    sys.exit(0)

def mainloop():
    while True:
        time.sleep(300)

if __name__ == "__main__":
    signal.signal(signal.SIGALRM, checkCommand)
    signal.signal(signal.SIGINT, quit)
    cfgobj = config.config()
    helper = helper.helper()
    verbose = cfgobj.getVerbose()
    signal.alarm(1)
    mainloop()
