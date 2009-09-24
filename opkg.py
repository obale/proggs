#!/usr/bin/python
# -*- coding: utf-8 -*-
# opkg.py - Searching packages on http://www.opkg.org
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
# hut WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>
import sys
import signal
import socket
from optparse import OptionParser
from xml.parsers import expat

class OPKGParser:
    def __init__(self, short):
        self._parser = expat.ParserCreate()
        self._parser.StartElementHandler = self.start
        self._parser.EndElementHandler = self.end
        if not short:
            self._parser.CharacterDataHandler = self.data
        else:
            self._parser.CharacterDataHandler = self.shortdata
        self._type = None

    def feed(self, data):
        self._parser.Parse(data, 0)

    def close(self):
        self._parser.Parse("", 1)
        del self._parser

    def start(self, tag, attrs):
        self._type = tag

    def end(self, tag):
        if ( tag == self._type ):
            self._type = None

    def data(self, data):
        RESET = "\033[0m"
        GREEN = "\033[1;32m"
        BLUE = "\033[1;34m"
        CYAN = "\033[1;36m"
        BOLD = "\033[1m"
        if ( self._type == 'name' ):
            print GREEN + '***********  ' + data,
            print '***********  ' + RESET
        elif ( self._type == 'homepage' ):
            print BOLD + 'homepage   : ' + RESET + CYAN + data + RESET
        elif ( self._type == 'developer' ):
            print BOLD + 'developer  : ' + RESET + data
        elif ( self._type == 'dependency' ):
            print BOLD + 'dependency : ' + RESET + data
        elif ( self._type == 'source' ):
            print BOLD + 'source     : ' + RESET + CYAN + data + RESET
        elif ( self._type == 'description_short' ):
            print BOLD + 'description: ' + RESET + data
        elif ( self._type == 'packagelink' ):
            print BOLD + 'packagelink: ' + RESET + CYAN + data + RESET
        elif ( self._type == 'category' ):
            print BOLD + 'category   : ' + RESET+ data
        elif ( self._type == 'version' ):
            print BOLD + 'version    : ' + RESET + data

    def shortdata(self, data):
        RESET = "\033[0m"
        GREEN = "\033[1;32m"
        if ( self._type == 'id'):
            print '[' + data + ']',
        elif ( self._type == 'name' ):
            print GREEN + data + RESET

class OPKGApi:
    def __init__(self):
        pass

    def getXMLByNumber(self, number):
        command = 'POST /api.php?action=show-package&pid=' + str(number) + ' HTTP/1.1\r\n'
        return self.getXML(command)

    def getXMLBySearchterm(self, searchterm):
        command = 'POST /api.php?action=search-package&q=' + searchterm + ' HTTP/1.1\r\n'
        return self.getXML(command)

    def getXMLAll(self):
        command = 'POST /api.php?action=list-all-packages HTTP/1.1\r\n'
        return self.getXML(command)

    def getXML(self, postcommand):
        self._soc = socket.socket()
        self._soc.connect( ('opkg.org', 80) )
        self._soc.send(postcommand)
        self._soc.send('Host: www.opkg.org\r\n\n')

        data = " "
        buffer = ""
        while data:
            data = self._soc.recv(1024)
            buffer += data
        self._soc.close()
        return self.parseAnswer(buffer)

    def parseAnswer(self, buffer):
        xmldata = buffer.split('<?xml version="1.0"?>')
        header = '<?xml version="1.0" encoding="latin1"?>'
        xmldata = header + xmldata[1]
        xmldata = xmldata.split('\r\n0\r\n\r\n')[0]
        return xmldata

class OPKG:
    def __init__(self):
        self._opkgapi = OPKGApi()

    def getPackageByNumber(self, number):
        data = self._opkgapi.getXMLByNumber(number)
        _opkgparser = OPKGParser(0)
        _opkgparser.feed(data)
        _opkgparser.close()

    def getPackageBySearchterm(self, searchterm):
        data = self._opkgapi.getXMLBySearchterm(searchterm)
        _opkgparser = OPKGParser(0)
        _opkgparser.feed(data)
        _opkgparser.close()

    def getAllPackages(self):
        data = self._opkgapi.getXMLAll()
        _opkgparser = OPKGParser(1)
        _opkgparser.feed(data)
        _opkgparser.close()

def sigint(signum, frame):
    print "Thank you for using this piece of software"
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint)
    parser = OptionParser()
    parser.add_option("-n", "--number", type="int", dest="number", help="Print information about the package NUMBER", metavar="NUMBER")
    parser.add_option("-s", "--search", type="str", dest="searchterm", help="Search for the PACKAGE", metavar="PACKAGE")
    parser.add_option("-a", "--all", action="store_true", dest="all", help="Show all packages in the list")

    (options, args) = parser.parse_args()

    opkg = OPKG()

    if options.number is not None:
        opkg.getPackageByNumber(options.number)
    elif options.searchterm is not None:
        opkg.getPackageBySearchterm(options.searchterm)
    elif options.all:
        opkg.getAllPackages()

