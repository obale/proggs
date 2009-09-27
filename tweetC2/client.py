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
import twitter
from optparse import OptionParser
from modules import config
from modules import commandParser
from modules import helper

# '\x00Today is really beautiful. We have here nice'
class tweetC2client:
    def __init__(self, username, password):
        cfg = config.config()
        self.accounts = cfg.getAccounts()
        self.prefix = cfg.getCommandPrefix()
        if password is None:
            password = self.getPassword(username)
        if password is None:
            helper.printErrorVerbose("No password for the user found!")
            sys.exit(0)
        self.api = twitter.Api(username, password)

    def getPassword(self, username):
        for account in self.accounts:
            if account[0] == username:
                return account[1]
        return None

    def sendMessage(self, command):
        command = self.prefix + command
        try:
            self.api.PostUpdate(command)
            helper.printInfoVerbose("Message send as command.")
        except:
            helper.printErrorVerbose("Message not send!")

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-u", "--user", type="str", dest="user", help="Specify \
an twitter USERNAME.", metavar="USERNAME")
    parser.add_option("-p", "--password", type="str", dest="pwd", help="Give \
the PASSWORD to the account. If not specified the password will be searched in the config file.", metavar="PASSWORD")
    parser.add_option("-m", "--message", type="str", dest="msg", help="The \
message which you would like to encode.")
    parser.add_option("-e", "--encode", action="store_true", dest="encode", \
help="Encode a message")

    (options, args) = parser.parse_args()

    helper = helper.helper()

    if options.user is not None and options.msg is not None:
        tweetobj = tweetC2client(options.user, options.pwd)
        tweetobj.sendMessage(options.msg)
    elif options.msg is not None and options.encode:
        parser = commandParser.commandParser()
        print parser.calcHash(self.prefix + options.msg)
    else:
        helper.printErrorVerbose("Please specify at least an user and a \
message or -e/--encode and a message.")

