# -*- coding: UTF-8 -*-
import string
import feedparser

def init(url):
    init.feed = feedparser.parse(url)

def getTitle():
    return init.feed['channel']['title']

def getEntries():
    msg = []
    count = 0
    for entry in init.feed['items']:
        if count == 10: break
        count += 1
        title = entry['title'].replace('\n', '')
        msg.append(str(count) + ': ' + title)
    return msg

def getEntry(number, feedname):
    url = getURL(feedname)
    if url is None:
        return getFeeds()
    init(url)
    nr = int(number) - 1
    msg =  []
    try:
        msg.append('Title: ' + init.feed['items'][nr]['title'])
        msg.append('URL  : ' + init.feed['items'][nr]['link'])
        try:
            summary = init.feed['items'][nr]['summary'][0:256]
            summary = summary.replace('\n', '')
            msg.append('Text : ' + summary)
        except KeyError:
            msg.append('Text : -')
    except IndexError:
        pass
    return msg

def getURL(feedname):
    if ( feedname == 'milworm' ):
        url = 'http://www.milw0rm.com/rss.php'
    elif ( feedname == 'heisesec' ):
        url = 'http://www.heise.de/security/news/news-atom.xml'
    elif ( feedname == 'sectube' ):
        url = 'http://feeds2.feedburner.com/SecurityTube'
    elif ( feedname == 'debsec' ):
        url = 'http://www.debian.org/security/dsa-long'
    elif ( feedname == 'ntv' ):
        url = 'http://www.n-tv.de/rss'
    elif ( feedname == 'n24' ):
        url = 'http://www.n24.de/2/index.rss'
    elif ( feedname == 'cnn' ):
        url = 'http://rss.cnn.com/rss/cnn_topstories.rss'
    elif ( feedname == 'prolinux' ):
        url = 'http://www.pro-linux.de/backend/pro-linux.rdf'
    elif ( feedname == 'isohunt' ):
        url = 'http://isohunt.com/js/rss/?iht='
    elif ( feedname == 'slashdot' ):
        url = 'http://rss.slashdot.org/Slashdot/slashdot'
    elif ( feedname == 'spiegel' ):
        url = 'http://www.spiegel.de/schlagzeilen/rss/index.xml'
    elif ( feedname == 'torrent' ):
        url = 'http://www.torrent.to/pub/XML/Last.rss.xml'
    elif ( feedname == 'bbc' ):
        url = 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/front_page/rss.xml'
    elif ( feedname == 'moksec' ):
        url = 'https://moksec.networld.to/trac/timeline?milestone=on&ticket=on&ticket_details=on&changeset=on&max=50&daysback=90&format=rss'
    elif ( feedname == 'sciencedaily' ):
        url = 'http://www.sciencedaily.com/rss/computers_math.xml'
    elif ( feedname == 'theregister' ):
        url = 'http://www.theregister.co.uk/headlines.atom'
    else:
        return None
    return url

def sendFeed(feedname):
    url = getURL(feedname)
    if url is None:
        return getFeeds()
    init(url)
    return getEntries()

def getFeeds():
    msg = []
    msg.append('-= Projects : moksec')
    msg.append('-= Security : milworm, heisesec, sectube, debsec')
    msg.append('-= News     : ntv, n24, spiegel, cnn, bbc, prolinux, slashdot')
    msg.append('-= Science  : sciencedaily, theregister')
    msg.append('-= Torrent  : isohunt, torrent')
    return msg