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
import string
import urllib
import lang

def getHeader(url):
    _ = lang.getGettext()
    if url is None:
        return [_("Not if anything to say about it!")]
    if not url.startswith('http://'):
        url = 'http://' + url
    urlfd = urllib.urlopen(url, proxies=None)
    header = urlfd.info()
    lines = string.split(str(header), '\r\n')
    urlfd.close()
    lines.remove("")
    return lines
