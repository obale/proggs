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
import random
import sqlite3
import time
import datetime
import lang
import helper
import tweet
import header
import search
import privateMessage
import feed

def greeting(soc, line):
    _ = lang.getGettext()
    msg = _('Hi ') + helper.getUser(line[0]) + _(' my friend. May the force be with you.')
    soc.send('PRIVMSG ' + helper.getUser(line[0]) + ' :' + msg + '\r\n')

def reactOnMSG(soc, line):
    _ = lang.getGettext()
    msg = []
    privmsg = line[3].strip(':')
    if ( privmsg == 'uptime' or privmsg == '!uptime' ):
        msg = _('Master Yoda long time here is. ')
        msg += getUptime()
        msg = [ msg ]
    elif ( privmsg == '!quote' ):
        msg = [ getQuote() ]
    elif ( privmsg == '!tweet' ):
        try:
            name = line[4]
        except Exception:
            name = None
        msg = [ tweet.getTimeline(name) ]
    elif ( privmsg == '!header' ):
        try:
            url = line[4]
        except Exception:
            url = None
        msg = header.getHeader(url)
    elif ( privmsg == '!search' or privmsg == '!google'):
        try:
            searchterm = line[4]
        except Exception:
            searchterm = None
        msg = search.getScroogle(searchterm)
    elif ( privmsg == '!msg' ):
        try:
            touser = line[4]
            message = line
            msg = []
            privateMessage.sendMessage(soc, helper.getUser(line[0]), touser, message)
        except:
            touser = None
            message = None
            msg = []
    elif ( privmsg == '!feed' ):
        try:
            feedname = line[4]
        except:
            feedname = None
            msg = feed.sendFeed(feedname)
        if feedname is not None:
            try:
                number = line[5]
                msg = feed.getEntry(number, feedname)
            except:
                msg = feed.sendFeed(feedname)
    elif ( privmsg == '!version' ):
        msg = helper.getVersion()
    else: msg = []
    for entry in msg:
        try:
            entry = entry.strip('\x00')
            entry = '\x02' + entry + '\x03'
            soc.send(bytearray('NOTICE ' + helper.getUser(line[0]) + ' :' + entry + '\r\n', 'utf-8'))
        except:
            pass

def getQuote():
    dbfile = helper.getDbfile()
    dbname = helper.getDbname()
    conn = sqlite3.connect(dbfile)
    #conn.text_factory = str
    curs = conn.cursor()

    query = "select min(id) from " + dbname
    curs.execute(query)
    minrow = int(curs.fetchone()[0])
    conn.commit()

    query = "select max(id) from " + dbname
    curs.execute(query)
    maxrow = int(curs.fetchone()[0])
    conn.commit()

    rand = random.randint(minrow, maxrow)
    query = "SELECT quote FROM " + dbname + " WHERE id=" + str(rand)
    curs.execute(query)
    quotes = curs.fetchone()[0]
    conn.commit()

    curs.close()
    return quotes

    rand = random.randint(1, 3)
    curs.execute("SELECT text FROM ? WHERE id=?", (self.DBNAME, rand) )
    quotes = curs.fetchone()

    conn.commit()
    curs.close()

    return quotes


def getUptime():
    _ = lang.getGettext()
    now = datetime.datetime.now()
    time = now - helper.getStarttime()
    weeks, days = divmod(time.days, 7)
    minutes, seconds = divmod(time.seconds, 60)
    hours, minutes = divmod(minutes, 60)

    msg = str(weeks) + _(' weeks, ')
    msg += str(days) + _(' days, ')
    msg += str(hours) + _(' hours, ')
    msg += str(minutes) + _(' minutes, ')
    msg += str(seconds) + _(' seconds.')

    return msg
