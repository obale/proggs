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
import os
import sys
import binascii
import ConfigParser

class config:
    configfile = "conf/tweetC2.cfg"
    defaultconfig = "conf/tweetC2.cfg.default"
    accounts = None

    def __init__(self):
        if os.path.exists(self.defaultconfig) and \
not os.path.exists(self.configfile):
            print "Please copy the file '" + self.defaultconfig + "' to '" + \
self.configfile + "'and edit it!"
            sys.exit(0)
        if not os.path.exists(self.defaultconfig) and \
not os.path.exists(self.configfile):
            print "There is no config file! Please contact the developer!"
            sys.exit(0)

        cfgparser = ConfigParser.SafeConfigParser()
        cfgparser.read(self.configfile)
        self.accounts = cfgparser.get('accounts', 'login')
        self.servers = cfgparser.get('server', 'connection')
        self.verbose = cfgparser.getboolean('tweetC2', 'verbose')
        self.color = cfgparser.getboolean('tweetC2', 'color')
        self.commandprefix = cfgparser.get('tweetC2', 'commandprefix')
        self.commandprefix = binascii.unhexlify(self.commandprefix)
        self.database = cfgparser.get('tweetC2', 'database')

    def getVerbose(self):
        return self.verbose

    def getColor(self):
        return self.color

    def getCommandPrefix(self):
        return unicode(self.commandprefix)

    def getDatabase(self):
        return self.database

    def getAccounts(self):
        self.accounts = self.accounts.split(',')
        result = []
        for account in self.accounts:
            account = account.strip()
            result.append(account.split(':'))
        return result

    def getServer(self):
        self.servers = self.servers.split(',')
        result = []
        for server in self.servers:
            server = server.strip()
            result.append(server.split(':'))
        return result

