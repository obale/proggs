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
import sqlite3
from optparse import OptionParser
from xml.parsers import expat

class OPKGParser:
    def __init__(self, short, color, save):
        self._type = None
        self._package = False
        self._parser = expat.ParserCreate()
        self._parser.StartElementHandler = self.start
        self._parser.EndElementHandler = self.end
        self._color = color
        self._save = save

        self._entry = self.getEmptyEntry()

        if self._save:
            self.createEmptyDatabase()
            self._parser.CharacterDataHandler = self.saveData
        else:
            if not short:
                self._parser.CharacterDataHandler = self.printData
            else:
                self._parser.CharacterDataHandler = self.printShortData

    def getEmptyEntry(self):
        return { 'id':None, 'name':None, 'homepage':None, \
                'developer':None, 'dependency':[], 'source': None,\
                'description':None, 'packagelink':None, 'category':None,\
                'version':None }

    def feed(self, data):
        self._parser.Parse(data, 0)

    def close(self):
        self._parser.Parse("", 1)
        del self._parser

    def start(self, tag, attrs):
        if ( tag == 'package' ):
            self._package = True
        self._type = tag

    def end(self, tag):
        if ( tag == self._type ):
            self._type = None
        if ( tag == 'package' ):
            self._package = False
            self.saveEntry(self._entry)
            del self._entry
            self._entry = self.getEmptyEntry()

    def printData(self, data):
        if self._color:
            RESET = "\033[0m"
            GREEN = "\033[1;32m"
            BLUE = "\033[1;34m"
            CYAN = "\033[1;36m"
            BOLD = "\033[1m"
        else:
            RESET = ""
            GREEN = ""
            BLUE = ""
            CYAN = ""
            BOLD = ""
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

    def printShortData(self, data):
        if self._color:
            RESET = "\033[0m"
            GREEN = "\033[1;32m"
        else:
            RESET = ""
            GREEN = ""
        if ( self._type == 'id'):
            print '[' + data + ']',
        elif ( self._type == 'name' ):
            print GREEN + data + RESET

    def saveData(self, data):
        if self._package:
            if ( self._type == 'id' ):
                self._entry['id'] = data
            elif ( self._type == 'name' ):
                self._entry['name'] = data
            elif ( self._type == 'homepage' ):
                self._entry['homepage'] = data
            elif ( self._type == 'developer' ):
                self._entry['developer'] = data
            elif ( self._type == 'dependency' ):
                self._entry['dependency'].append(data)
            elif ( self._type == 'source' ):
                self._entry['source'] = data
            elif ( self._type == 'description_short' ):
                self._entry['description_short'] = data
            elif ( self._type == 'packagelink' ):
                self._entry['packagelink'] = data
            elif ( self._type == 'category' ):
                self._entry['category'] = data
            elif ( self._type == 'version' ):
                self._entry['version'] = data

    def saveEntry(self, entry):
        conn = sqlite3.connect('opkg.db')
        conn.text_factory = str
        curs = conn.cursor()
        query = 'INSERT INTO packages VALUES ( '
        query += entry['id'] + ', '
        query += '"' + entry['name'] + '", '
        query += '"' + str(entry['homepage']) + '", '
        if entry['developer'] is not None:
            query += '"' + entry['developer'] + '", '
        else:
            query += '"", '
        dependency = ''
        for line in entry['dependency']:
            dependency += line + ' '
        query += '"' + str(dependency) + '", '
        query += '"' + str(entry['source']) + '", '
        if entry['description_short'] is not None:
            query += '"' + entry['description_short'] + '", '
        else:
            query += '"", '
        query += '"' + str(entry['packagelink']) + '", '
        query += '"' + str(entry['category']) + '", '
        query += '"' + str(entry['version']) + '"'
        query += ')'
        print query
        curs.execute(query)
        conn.commit()
        curs.close()

    def createEmptyDatabase(self):
        conn = sqlite3.connect('opkg.db')
        curs = conn.cursor()
        try:
            curs.execute('DROP TABLE packages')
        except sqlite3.OperationalError:
            pass
        curs.execute('CREATE TABLE packages (id INTEGER, name VARCHAR, homepage VARCHAR, \
developer VARCHAR, dependency VARCHAR, source VARCHAR, description_short VARCHAR, \
packagelink VARCHAR, category VARCHAR, version VARCHAR)')
        conn.commit()
        curs.close()

class OpkgXml:
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
        self._opkgxml = OpkgXml()
        self._color = True
        self._nocolor = not self._color
        self._save = True
        self._nosave = not self._save

    def getPackageByNumber(self, number):
        data = self._opkgxml.getXMLByNumber(number)
        _opkgparser = OPKGParser(False, self._color, self._nosave)
        _opkgparser.feed(data)
        _opkgparser.close()

    def getPackageBySearchterm(self, searchterm):
        data = self._opkgxml.getXMLBySearchterm(searchterm)
        _opkgparser = OPKGParser(False, self._color, self._nosave)
        _opkgparser.feed(data)
        _opkgparser.close()

    def getAllPackages(self):
        data = self._opkgxml.getXMLAll()
        _opkgparser = OPKGParser(True, self._color, self._nosave)
        _opkgparser.feed(data)
        _opkgparser.close()

    def savePackages(self):
        data = self._opkgxml.getXMLAll()
        _opkgparser = OPKGParser(None, self._nocolor, self._save)
        _opkgparser.feed(data)
        _opkgparser.close()

def sigint(signum, frame):
    print "Thank you for using this piece of software"
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint)
    parser = OptionParser()
    parser.add_option("-n", "--number", type="int", dest="number", help="print information about the package NUMBER", metavar="NUMBER")
    parser.add_option("-s", "--search", type="str", dest="searchterm", help="search for the PACKAGE", metavar="PACKAGE")
    parser.add_option("-a", "--all", action="store_true", dest="all", help="show all packages in the list")
    parser.add_option("-u", "--update", action="store_true", dest="update", help="update the local database")
    parser.add_option("-i", "--install", action="store_true", dest="install", help="install the package")

    (options, args) = parser.parse_args()

    opkg = OPKG()

    if options.update:
        opkg.savePackages()
    elif options.install:
        print "Install package. [NOT IMPLEMTED]"
    elif options.number is not None:
        opkg.getPackageByNumber(options.number)
    elif options.searchterm is not None:
        opkg.getPackageBySearchterm(options.searchterm)
    elif options.all:
        opkg.getAllPackages()

