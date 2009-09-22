#!/usr/bin/python
# -*- coding: UTF-8 -*-
# ircbot.py - A simple IRC bot
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
import os
import signal
import string
from modules import helper
from modules import react
from modules import lang
from modules import logger

class IRCBot:
    """
    A IRC bot written from scratch.
    Functionality:
        
        * Greeting if somebody comes to the cannel (query)
        * Quotes (query/channel)
        * uptime (query/channel)
        * logging
        * config
        * multilanguage (de/en)
    """
    global _

    global DBFILE, DBNAME
    global starttime

    def __init__(self):
        lang.init()
        self._ = lang.getGettext()
        signal.signal(signal.SIGINT, self.clean)
        helper.connect()
        logger.init()
        self.loop()

    def loop(self):
        soc = helper.getSocket()
        nickname = helper.getNickname()
        channel = helper.getChannel()

        readbuffer = ""
        while 1:
            readbuffer = readbuffer + soc.recv(1024)
            tmp = string.split(readbuffer, '\n')
            readbuffer = tmp.pop()

            for line in tmp:
                logger.logging(line)
                line = string.rstrip(line)
                line = string.split(line)

                try:
                    if ( helper.getUser(line[0]) != nickname and line[1] == 'PRIVMSG' and line[2] == nickname ):
                        react.reactOnPRIVMSG(soc, line)
                    elif ( helper.getUser(line[0]) != nickname and line[1] == 'PRIVMSG' and line[2] == channel ):
                        react.reactOnMSG(soc, line)
                    elif ( helper.getUser(line[0]) != nickname and line[1] == 'JOIN' ):
                        react.greeting(soc, line)
                except Exception:
                    pass

                if ( line[0] == 'PING' ):
                    soc.send('PONG ' + line[1] + '\r\n')

    def clean(self, signum, frame):
        soc = helper.getSocket()
        soc.send('QUIT :Bot is leaving the house!\r\n')
        sys.exit(0)

if __name__ == "__main__":
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        print >> sys.stderr, "fork failed: %d (%s)" % (e.errno, e.strerror)
        sys.exit(1)
    #os.chdir('/')
    os.setsid()
    os.umask(0)
    IRCBot()
