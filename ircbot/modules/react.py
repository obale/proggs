# -*- coding: UTF-8 -*-
import random
import sqlite3
import time
import datetime
import lang
import helper
import tweet

def greeting(soc, line):
    _ = lang.getGettext()
    msg = _('Hi ') + helper.getUser(line[0]) + _(' my friend. May the force be with you.')
    soc.send('PRIVMSG ' + helper.getUser(line[0]) + ' :' + msg + '\r\n')

def reactOnPRIVMSG(soc, line):
    _ = lang.getGettext()
    privmsg = line[3].strip(':')
    if ( privmsg == 'uptime' ):
        msg = _('Master Yoda long time here is. ')
        msg += getUptime()
    elif ( privmsg == 'quote' ):
        msg = getQuote()
    elif ( privmsg == 'tweet' ):
        try:
            name = line[4]
        except Exception:
            name = None
        msg = tweet.getTimeline(name)
    else:
        msg = _('Not if anything to say about it!')
    soc.send('PRIVMSG ' + helper.getUser(line[0]) + ' :' + msg + '\r\n')

def reactOnMSG(soc, line):
    _ = lang.getGettext()
    channel = helper.getChannel()
    privmsg = line[3].strip(':')
    if ( privmsg == '!uptime' ):
        msg = _('Master Yoda long time here is. ')
        msg += getUptime()
    elif ( privmsg == '!quote' ):
        msg = getQuote()
    elif ( privmsg == '!tweet' ):
        try:
            name = line[4]
        except Exception:
            name = None
        msg = tweet.getTimeline(name)
    else:
        return
    soc.send('PRIVMSG ' + channel + ' :' + msg + '\r\n')

def getQuote():
    dbfile = helper.getDbfile()
    dbname = helper.getDbname()
    conn = sqlite3.connect(dbfile)
    conn.text_factory = str
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
