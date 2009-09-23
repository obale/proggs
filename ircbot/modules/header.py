# -*- coding: UTF-8 -*-
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
