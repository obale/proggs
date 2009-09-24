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
import helper

def sendCommandPRIVMSG(soc, user, command):
    soc.send(bytearray('PRIVMSG ' + user + ' :\x01' + command + '\x01\r\n'))

def sendCommandNOTICE(soc, user, command):
    soc.send(bytearray('NOTICE ' + user + ' :\x01' + command + '\x01\r\n'))

def inqVERSION(soc, user):
    sendCommandPRIVMSG(soc, user, 'VERSION')

def inqUSERINFO(soc, user):
    sendCommandPRIVMSG(soc, user, 'USERINFO')

def inqFINGER(soc, user):
    sendCommandPRIVMSG(soc, user, 'FINGER')

def inqCLIENTINFO(soc, user):
    sendCommandPRIVMSG(soc, user, 'CLIENTINFO')

def inqTIME(soc, user):
    sendCommandPRIVMSG(soc, user, 'TIME')

def inqSOURCE(soc, user):
    sendCommandPRIVMSG(soc, user, 'SOURCE')

def checkCTCP(soc, user, command):
    if ( command == ':\x01VERSION\x01' ):
        sendCommandPRIVMSG(soc, user, 'VERSION :ircbot:v0.01:linux')
    elif ( command == ':\x01USERINFO\x01' ):
        sendCommandPRIVMSG(soc, user, 'USERINFO :I\'m a python bot written from scratch.')
    elif ( command == ':\x01TIME\x01' ):
        sendCommandPRIVMSG(soc, user, 'TIME :' + helper.getTime() )
    # XXX: Prints on every message in query, except from the three (3) cases
    #      above. It should only print this message if there is an unknown
    #      ctcp message, not always.
    #else:
        #newcommand = command.strip(':\x01')
        #sendCommandNOTICE(soc, user, ':\x01ERRMSG ' + newcommand + ' :Query is unknown\x01')
