#!/usr/bin/python
# -*- coding: utf-8 -*-
from optparse import OptionParser
from xml.parsers import expat
import socket

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
        if ( self._type == 'name' ):
            print '***********  ' + data,
            print '***********  '
        elif ( self._type == 'homepage' ):
            print 'homepage   : ' + data
        elif ( self._type == 'developer' ):
            print 'developer  : ' + data
        elif ( self._type == 'dependency' ):
            print 'dependency : ' + data
        elif ( self._type == 'source' ):
            print 'source     : ' + data
        elif ( self._type == 'description_short' ):
            print 'description: ' + data
        elif ( self._type == 'packagelink' ):
            print 'packagelink: ' + data
        elif ( self._type == 'category' ):
            print 'category   : ' + data

    def shortdata(self, data):
        if ( self._type == 'name' ):
            print data
        elif ( self._type == 'id'):
            print '[' + data + '] ',

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
            data = self._soc.recv(512)
            buffer += data
        self._soc.close()
        return self.parseAnswer(buffer)

    def parseAnswer(self, buffer):
        xmldata = buffer.split('<?xml version="1.0"?>')
        header = '<?xml version="1.0"?>'
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

if __name__ == "__main__":
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

