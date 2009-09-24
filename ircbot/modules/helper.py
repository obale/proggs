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
import socket
import datetime
import ConfigParser

def readConfig():
    config = ConfigParser.SafeConfigParser()
    config.read('conf/ircbot.cfg')
    readConfig.HOST = config.get('server', 'host')
    readConfig.PORT = config.getint('server', 'port')
    readConfig.PASS = config.get('server', 'password')
    readConfig.NICKNAME = config.get('bot', 'nickname')
    readConfig.FULLNAME = config.get('bot', 'fullname')
    readConfig.IDENT = config.get('bot', 'ident')
    readConfig.CHANNEL = config.get('channel', 'mainchannel')
    readConfig.DBFILE = config.get('quotes', 'dbfile')
    readConfig.DBNAME = config.get('quotes', 'dbname')
    readConfig.LOGGING = config.getboolean('server', 'logging')
    if readConfig.LOGGING:
        readConfig.LOGFILE = config.get('server', 'logfile')

def connect():
    readConfig()
    connect.soc = socket.socket()
    connect.soc.connect( (readConfig.HOST, readConfig.PORT) )
    connect.soc.send('PASS ' + readConfig.PASS + '\r\n')
    connect.soc.send('USER ' + readConfig.IDENT + ' 8 * :' + readConfig.FULLNAME + '\r\n')
    connect.soc.send('NICK ' + readConfig.NICKNAME + '\r\n')
    connect.starttime = datetime.datetime.now()
    joinMainchannel()

def joinMainchannel():
    connect.soc.send('JOIN ' + readConfig.CHANNEL + '\r\n')

def getSocket():
    return connect.soc

def getNickname():
    return readConfig.NICKNAME

def getChannel():
    return readConfig.CHANNEL

def getDbfile():
    return readConfig.DBFILE

def getDbname():
    return readConfig.DBNAME

def getLogging():
    return readConfig.LOGGING

def getLogfile():
    assert readConfig.LOGGING
    return readConfig.LOGFILE

def getStarttime():
    return connect.starttime

def getTime():
    dt = datetime.datetime.now()
    return dt.strftime("%A, %d. %B %Y %H:%M")

def getUser(line):
    user = line.strip(':')
    user = user.split('!')
    return user[0]

def getVersion():
    msg = []
    msg.append("Master Yoda (IRC Bot)")
    msg.append("          .--.")
    msg.append("::\`--._,'.::.`._.--'/::::")
    msg.append("::::.  ` __::__ '  .::::::")
    msg.append("::::::-:.`'..`'.:-::::::::")
    msg.append("::::::::\ `--' /::::::::::")
    msg.append("          `--'")
    msg.append("by Alex Oberhauser")
    msg.append("http://irc.networld.to")

    return msg

