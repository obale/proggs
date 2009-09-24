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
import datetime
import sqlite3
import ConfigParser
import lang
import string

def init():
    config = ConfigParser.SafeConfigParser()
    config.read('conf/ircbot.cfg')
    init.DBFILE = config.get('privatemessage', 'dbfile')
    init.DBNAME = config.get('privatemessage', 'dbname')
    dt = datetime.datetime.now()
    init.NOW = dt.strftime("%A, %d. %B %Y %H:%M")
    init.conn = sqlite3.connect(init.DBFILE)
    init.conn.text_factory = str
    init.curs = init.conn.cursor()

def clean():
    init.conn.commit()
    init.curs.close()

def sendMessage(soc, fromuser, touser, line):
    fromuser = string.lower(fromuser)
    touser = string.lower(touser)
    _ = lang.getGettext()
    message = ""
    for msg in line:
        if msg == line[0] or msg == line[1] or msg == line[2] or msg == line[3] or msg == line[4]: continue
        msg = string.strip(msg, '["\']')
        message += msg + " "
    if message == "":
        return
    init()
    query = "INSERT INTO " + init.DBNAME + " ( fromuser, touser, time, message )"
    query += "VALUES ( '" + fromuser + "', '" + touser + "', '" + init.NOW + "', '" + message + "')"
    try:
        init.curs.execute(query)
    except Exception:
        errmsg = _('Error there is occurred!')
        soc.send('PRIVMSG ' + fromuser + ' :'+ errmsg + '\r\n')
    msg = _('Sent!')
    soc.send('PRIVMSG ' + fromuser + ' :'+ msg + '\r\n')
    clean()

def receiveMessages(soc, touser):
    touser = string.lower(touser)
    init()
    query = "SELECT fromuser, time, message FROM " + init.DBNAME + " where touser='" + touser + "'"
    init.curs.execute(query)
    for row in init.curs:
        msg = "[" + row[1] + "] by " + row[0] + ": " + row[2]
        soc.send('NOTICE ' + touser + ' :' + msg + '\r\n')
    query = "DELETE FROM " + init.DBNAME + " where touser=\"" + touser + "\""
    init.curs.execute(query)
    clean()

