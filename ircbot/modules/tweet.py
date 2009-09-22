# -*- coding: UTF-8 -*-
import twitter
import lang

def getTimeline(name):
    _ = lang.getGettext()
    if name is None:
        return _("Not if anything to say about it!")
    api = twitter.Api()
    statuses = api.GetUserTimeline(name, count=1)
    return statuses[0].text + " [" +statuses[0].created_at + "]"
