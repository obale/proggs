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
import config

class helper:
    def __init__(self):
        cfg = config.config()
        self.verbose = cfg.getVerbose()
        self.color = cfg.getColor()

    def printInfoVerbose(self, msg):
        if self.color and self.verbose:
            print "\033[0;33m[INFO]\033[m " + msg
        elif self.verbose:
            print "[INFO] " + msg

    def printInfo(self, msg):
        if self.color:
            print "\033[0;33m[INFO]\033[m " + msg
        else:
            print "[INFO] " + msg

    def printErrorVerbose(self, msg):
        if self.color and self.verbose:
            print "\033[1;31m[ERROR]\033[m " + msg
        elif self.verbose:
            print "[ERROR] " + msg

    def printError(self, msg):
        if self.color:
            print "\033[1;31m[ERROR]\033[m " + msg
        else:
            print "[ERROR] " + msg

    def printHitVerbose(self, username, command):
        if self.color and self.verbose:
            print "\033[0;32m[HIT]\033[m  " + username + " send \033[1m" + command + "\033[m."
        elif self.verbose:
            print "[HIT]  " + username + " send " + command + "."

    def printHit(self, username, command):
        if self.color:
            print "\033[0;32m[HIT]\033[m  " + username + " send \033[1m" + command + "\033[m."
        else:
            print "[HIT]  " + username + " send " + command + "."

