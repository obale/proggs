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
import string, random
import ConfigParser
import datetime, time

class IRCBot:
    """
    A very simple IRC bot written from scratch
    """

    global HOST, PORT, PASS
    global NICKNAME, IDENT, FULLNAME
    global CHANNEL
    global LOGGING, LOGFILE
    global starttime

    global socket

    def __init__(self):
        self.starttime = datetime.datetime.now()
        config = ConfigParser.SafeConfigParser()
        config.read('./ircbot.cfg')
        self.HOST = config.get('server', 'host')
        self.PORT = config.getint('server', 'port')
        self.PASS = config.get('server', 'password')
        self.NICKNAME = config.get('bot', 'nickname')
        self.FULLNAME = config.get('bot', 'fullname')
        self.IDENT = config.get('bot', 'ident')
        self.CHANNEL = config.get('channel', 'mainchannel')
        self.LOGGING = config.getboolean('server', 'logging')
        if self.LOGGING:
            self.LOGFILE = config.get('server', 'logfile')
            file = open(self.LOGFILE, 'a')
            dt = datetime.datetime.now()
            now = dt.strftime("%A, %d. %B %Y %H:%M")
            str = '======================== BEGIN LOGIN: ' + now \
+ ' ========================\n'
            file.write(str)
            file.close()

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
        privmsg = line[3].strip(':')
        if ( privmsg == 'uptime' ):
            msg = 'Master Yoda long time here is. '
            msg += self.getUptime()
        elif ( privmsg == 'quote' ):
            msg = self.getQuote()
        else:
            msg = 'Not if anything to say about it!'
        self.socket.send('PRIVMSG ' + self.getUser(line[0]) + ' :' + msg + '\r\n')

    def reactOnMSG(self, line):
        privmsg = line[3].strip(':')
        if ( privmsg == '!uptime' ):
            msg = 'Master Yoda long time here is. '
            msg += self.getUptime()
        elif ( privmsg == '!quote' ):
            msg = self.getQuote()
        else:
            return
        self.socket.send('PRIVMSG ' + self.CHANNEL + ' :' + msg + '\r\n')

    def getQuote(self):
        quotes = [ ]
        quotes.append("Agree with you, the council does. Your apprentice, Skywalker will be.")
        quotes.append("Always two there are, no more, no less: a master and an apprentice.")
        quotes.append("Fear is the path to the Dark Side. Fear leads to anger, anger leads to hate; hate leads to suffering. I sense much fear in you." )
        quotes.append("Qui-Gon's defiance I sense in you.")
        quotes.append("Truly wonderful the mind of a child is.")
        quotes.append("Around the survivors a perimeter create.")
        quotes.append("Lost a planet Master Obi-Wan has. How embarrassing ... how embarrassing.")
        quotes.append("Victory, you say? Master Obi-Wan, not victory. The shroud of the Dark Side has fallen. Begun the Clone War has.")
        quotes.append("Much to learn you still have ... my old padawan. ... This is just the beginning!")
        quotes.append("Twisted by the Dark Side young Skywalker has become.")
        quotes.append("The boy you trained, gone he is, consumed by Darth Vader.")
        quotes.append("Death is a natural part of life. Rejoice for those around you who transform into the Force. Mourn them do not. Miss them do not. Attachment leads to jealousy. The shadow of greed that is. Train yourself to let go of everything you fear to lose.")
        quotes.append("The fear of loss is a path to the Dark Side.")
        quotes.append("If into the security recordings you go, only pain will you find.")
        quotes.append("Not if anything to say about it I have")
        quotes.append("Great warrior, hmm? Wars not make one great.")
        quotes.append("Do or do not; there is no try.")
        quotes.append("Size matters not. Look at me. Judge me by my size, do you?")
        quotes.append("That is why you fail.")
        quotes.append("No! No different. Only different in your mind. You must unlearn what you have learned.")
        quotes.append("Always in motion the future is.")
        quotes.append("Reckless he is. Matters are worse.")
        quotes.append("No. There is another. ...")
        quotes.append("When nine hundred years old you reach, look as good, you will not.")
        quotes.append("There is ... another ... Sky ... walker. ...")
        quotes.append("When 900 years old you reach, look as good you will not ehh.")
        rand = random.randint(0, 3)
        return quotes[rand]

    def greeting(self, line):
        msg = 'Hi ' + self.getUser(line[0]) + ' my friend. May the force be with you.'
        self.socket.send('PRIVMSG ' + self.getUser(line[0]) + ' :' + msg + '\r\n')

    def logging(self, line):
        if not self.LOGGING:
            return
        file = open(self.LOGFILE, 'a')
        file.write(line + '\n')
        file.close

    def getUser(self, line):
        user = line.strip(':')
        user = user.split('!')
        return user[0]

    def getUptime(self):
        now = datetime.datetime.now()
        time = now - self.starttime

        weeks, days = divmod(time.days, 7)
        minutes, seconds = divmod(time.seconds, 60)
        hours, minutes = divmod(minutes, 60)

        msg = str(weeks) + ' weeks, '
        msg += str(days) + ' days, '
        msg += str(hours) + ' hours, '
        msg += str(minutes) + ' minutes, '
        msg += str(seconds) + ' seconds.'

        return msg

    def loop(self):
        readbuffer = ""
        while 1:
            readbuffer = readbuffer + self.socket.recv(1024)
            tmp = string.split(readbuffer, '\n')
            readbuffer = tmp.pop()

            for line in tmp:
                self.logging(line)
                line = string.rstrip(line)
                line = string.split(line)

                try:
                    if ( self.getUser(line[0]) != self.NICKNAME and line[1] == 'PRIVMSG' and line[2] == self.NICKNAME ):
                        self.reactOnPRIVMSG(line)
                    elif ( self.getUser(line[0]) != self.NICKNAME and line[1] == 'PRIVMSG' and line[2] == self.CHANNEL):
                        self.reactOnMSG(line)
                    elif ( self.getUser(line[0]) != self.NICKNAME and line[1] == 'JOIN' ):
                        self.greeting(line)
                except Exception:
                    pass

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
    #os.chdir('/')
    os.setsid()
    os.umask(0)
    IRCBot()
