# kismet2tangogps.py
#
# (C) 2008 by Networld Consulting, Ltd.
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
# You should have received a copy of the GNU General Public License.  
# If not, see <http://www.gnu.org/licenses/>
from pysqlite2 import dbapi2 as sqlite
import time

class K2P:
    """
    A simple python script which converts the Kismet way points to tangogps
    POI

    @param1 The filename with the coordinates and the hotspot name.
            Format is: name lat lon
            The name shouldn't have spaces and lat/lon are float values.
    @param1 The sqlite database file in where you would like to save the
            coordinates. Must be a valid tangogps poi database file.
    """
    def __init__(self, filename, sqlitedb):
        self.parse_file(filename, sqlitedb)

    def parse_file(self, filename, sqlitedb):
        try:
            fd = open(filename, 'r')
            lines = fd.readlines()
        except IOError:
            print 'cannont open', file
            sys.exit(1)

        for line in lines:
            if line.find(" ") > -1:
                data = line.split()
                essid = data[0]
                lat = data[1]
                lon = data[2]
                self.add_to_db(sqlitedb, essid, lat, lon)

        fd.close()


    def add_to_db(self, sqlitedb, essid, lat, lon):
        conn = sqlite.connect(sqlitedb, isolation_level=None)
        curr_time = time.time()  # The current time for the 
        visible = 0              # Is the POI visible for others
        cat = 10                 # The Category.    10 ... 'Services'
        subcat = 1               # The Subcategory.  1 ... 'Wifi Hotspot'
        desc = 'Wifi Hotspot added by the kismet2tangogps.py script'
        creator = 'kismet/kismet2tangogps.py'
        stmt = 'INSERT INTO poi (idmd5, lat, lon, visibility, cat, subcat, keywords, desc, price_range, extended_open, creator) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        ret = conn.execute(stmt, ('%s' % curr_time, lat, lon, visible, cat, subcat, essid, desc, 3, 0, creator)).rowcount > 0
        conn.commit()
        conn.close()


FILENAME = '/home/obale/.gpsdrive/way_kismet.txt'
SQLITEDB = '/home/obale/.tangogps/poi.db'

k2p = K2P(FILENAME, SQLITEDB)
