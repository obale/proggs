#!/usr/bin/python
# scanMSN.py - A MSN contact list parser on the base of the scapy framework.
#
# (C) 2008 by MokSec Project
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
import sys
import re
from scapy.all import *

class scanMSN:
    global packets

    def __init__(self):
        self.packets = None
        print

    def scan(self):
        seconds = self.readSeconds()
        print "==> NOTICE: Starting the sniffing for " + str(seconds) + " seconds."
        self.packets = sniff(timeout=seconds)

    def filterContacts(self):
        if self.packets is None:
            print "!=> ERROR: There are no packets to filter."
            return

        for p in self.packets:
            pkgload = str(p.payload)
            try:
                srcip = p.getlayer(IP).src
                dstip = p.getlayer(IP).dst
            except Exception:
                pass
            result = re.search("(<ml l='1'><d n='execs.com'>.*</ml>)", pkgload)
            if result is not None:
                self.parseContacts(result.group(0), srcip, dstip)

    def parseContacts(self, _payload, _srcip, _dstip):
       print
       result = re.findall(r"<c n='[a-zA-Z0-9]*' l='.' t='.'/>", _payload)
       print "=== MSN contacts send from " + _srcip + " to " + _dstip + " ==="
       for entry in result:
           entry = re.search("'[a-zA-Z0-9]+'", entry)
           print entry.group(0)


    def readSeconds(self):
        if len(sys.argv) != 2:
            self.help()
            sys.exit(0)
        else:
            seconds = int(sys.argv[1])
        return seconds

    def help(self):
        print "Usage: " + sys.argv[0] + " <seconds>"
        print "   eg: " + sys.argv[0] + " 60"

obj = scanMSN()
obj.scan()
obj.filterContacts()
