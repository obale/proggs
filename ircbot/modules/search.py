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
import re
import socket
import ssl

def getScroogle(searchterm):
        HOST = 'ssl.scroogle.org'
        PORT = 443
        soc = socket.socket()
        sslsoc = ssl.wrap_socket(soc)

        sslsoc.connect( (HOST, PORT) )
        sslsoc.send('POST /cgi-bin/nbbwssl.cgi?Gw=' + searchterm + '\r\n')
        sslsoc.send('Host: ssl.scroogle.org\r\n\n')

        result0 = sslsoc.recv(1024)
        result1 = result0.lower()
        result = re.findall("http[s]*://[a-zA-Z$-_.+!*'(),?;]*", result1)

        return [ result[1] ]
