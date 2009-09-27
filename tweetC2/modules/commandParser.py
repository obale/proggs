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
import hashlib
import config

class commandParser:
    def __init__(self):
        # '\x00Testing' -> 'cmd_testing'
        # '\x00Hello'   -> 'cmd_hello'
        cfg = config.config()
        self.prefix = cfg.getCommandPrefix()
        print self.prefix
        self.commands = { \
                '83f5e02544456916446b44057dfb93efafd0b27a36e085eb9d587d440c7cc810b499b4a3b86e697c9527b8eb3dde3e3a0853c28b4d83f6fdd2a58c2fc9eb0ac1':'cmd_testing',\
                '3ba02f42ea31e8269c06cfc57bcb47c31fa5150125b8b8018a07423e5287b12e8253bc73d424f21f742e9eab09408b8eca1c980527ba712fe8759936669cd2e2':'cmd_hello'\
                }


    def calcHash(self, command):
        sha = hashlib.sha512()
        sha.update(command)
        return sha.hexdigest()

    def checkCommand(self, command):
        if command[0] != self.prefix:
            return None
        try:
            return self.commands[self.calcHash(command)]
        except:
            return None
