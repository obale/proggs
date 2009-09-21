#!/usr/bin/python
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
import sys, os, signal, socket
import string
import ConfigParser

class IRCBot:

    global HOST, PORT, PASS
    global NICKNAME, IDENT, FULLNAME
    global CHANNEL

    global socket

    def __init__(self):
        config = ConfigParser.SafeConfigParser()
        config.read('ircbot.cfg')
        self.HOST = config.get('server', 'host')
        self.PORT = int(config.get('server', 'port'))
        self.PASS = config.get('server', 'password')
        self.NICKNAME = config.get('bot', 'nickname')
        self.FULLNAME = config.get('bot', 'fullname')
        self.IDENT = config.get('bot', 'ident')
        self.CHANNEL = config.get('channel', 'mainchannel')

        signal.signal(signal.SIGINT, self.clean)

        self.connect()

    def connect(self):
        self.socket = socket.socket()
        self.socket.connect( (self.HOST, self.PORT) )
        self.socket.send('PASS ' + self.PASS + '\r\n')
        self.socket.send('USER ' + self.IDENT + ' 8 * :' + self.FULLNAME + '\r\n')
        self.socket.send('NICK ' + self.NICKNAME + '\r\n')
        self.joinMainchannel()
        self.loop()

    def joinMainchannel(self):
        self.socket.send('JOIN ' + self.CHANNEL + '\r\n')

    def reactOnPRIVMSG(self, line):
        try:
            if ( line[1] == 'PRIVMSG' and line[2] == 'yoda' ):
                        str = "Sorry dude, at the moment I'm very dump and can't react on your message :("
                        user = line[0].strip(':')
                        user = user.split('!')
                        self.socket.send('PRIVMSG ' + user[0] + ' :' + str + '\r\n')
        except Exception:
            pass

    def printLine(self, line):
        print line

    def loop(self):
        readbuffer = ""
        while 1:
            readbuffer = readbuffer + self.socket.recv(1024)
            tmp = string.split(readbuffer, '\n')
            readbuffer = tmp.pop()

            for line in tmp:
                ## XXX: In productive use we don't want that the bot prints
                ##      all stuff.
                #self.printLine(line)
                line = string.rstrip(line)
                line = string.split(line)

                self.reactOnPRIVMSG(line)

                if ( line[0] == 'PING' ):
                    self.socket.send('PONG ' + line[1] + '\r\n')

    def clean(self, signum, frame):
        self.socket.send('QUIT :Bot is leaving the house!\r\n')
        sys.exit(0)

if __name__ == "__main__":
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        print >> sys.stderr, "fork failed: %d (%s)" % (e.errno, e.strerror)
        sys.exit(1)
    obj = IRCBot()


