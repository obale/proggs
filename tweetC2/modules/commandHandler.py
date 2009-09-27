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
import commandParser
import twitterApi
import config
import sqlite3
import helper

class commandHandler:
    def __init__(self):
        self.cmdparser = commandParser.commandParser()
        self.twapi = twitterApi.twitterApi()
        self.cfg = config.config()
        self.verbose = self.cfg.getVerbose()
        self.helper = helper.helper()

    def handleCommand(self):
        entries = self.twapi.getLastEntry()
        for entry in entries:
            if self.checkCommandHandled(entry):
                return
            if 'cmd_testing' == self.cmdparser.checkCommand(entry[1]):
                self.helper.printHitVerbose(entry[0], 'cmd_testing')
                self.setCommandHandled(entry)
            elif 'cmd_hello' == self.cmdparser.checkCommand(entry[1]):
                self.helper.printHitVerbose(entry[0], 'cmd_hallo')
                self.setCommandHandled(entry)

    def setCommandHandled(self, entry):
        conn = sqlite3.connect(self.cfg.getDatabase())
        conn.text_factory = str
        curs = conn.cursor()
        curs.execute('INSERT INTO handled_commands (username, message,\
created_at) VALUES ( ?, ?, ?)', (entry[0], repr(entry[1]), entry[2] ))
        conn.commit()
        curs.close()

    def checkCommandHandled(self, entry):
        conn = sqlite3.connect(self.cfg.getDatabase())
        conn.text_factory = str
        curs = conn.cursor()
        curs.execute('SELECT username, message, created_at FROM \
handled_commands')
        for row in curs:
            if row[0] == entry[0] and row[1] == repr(entry[1]) and row[2] == entry[2]:
                return True
        conn.commit()
        curs.close()
        return False
