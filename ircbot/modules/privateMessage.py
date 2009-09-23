# -*- coding: UTF-8 -*-
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
    init.curs = init.conn.cursor()

def clean():
    init.conn.commit()
    init.curs.close()

def sendMessage(soc, fromuser, touser, line):
    _ = lang.getGettext
    message = ""
    for msg in line:
        if msg == line[0] or msg == line[1] or msg == line[2] or msg == line[3] or msg == line[4]: continue
        msg = string.strip(msg, '["\']')
        message += msg + " "
    init()
    query = "INSERT INTO " + init.DBNAME + " ( fromuser, touser, time, message )"
    query += "VALUES ( '" + fromuser + "', '" + touser + "', '" + init.NOW + "', '" + message + "')"
    try:
        init.curs.execute(query)
    except Exception:
        soc.send('PRIVMSG ' + fromuser + ' :Error!\r\n')
    clean()

def receiveMessages(soc, touser):
    init()
    query = "SELECT fromuser, time, message FROM " + init.DBNAME + " where touser='" + touser + "'"
    init.curs.execute(query)
    for row in init.curs:
        msg = "[" + row[1] + "] by " + row[0] + ": " + row[2]
        soc.send('PRIVMSG ' + touser + ' :' + msg + '\r\n')
    query = "DELETE FROM " + init.DBNAME + " where touser=\"" + touser + "\""
    init.curs.execute(query)
    clean()

