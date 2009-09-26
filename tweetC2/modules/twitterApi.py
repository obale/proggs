#!/usr/bin/python
# -*- coding: UTF-8 -*-
# tweetC2 - A twitter bot, which handles commands and reacts on it. 
#           (C2 = command & control)
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
import twitter
import config

class twitterApi:
    def __init__(self):
        cfg = config.config()
        self.accounts = cfg.getAccounts()
        self.pubapi = twitter.Api()

    def getLastEntry(self):
        result = []
        for account in self.accounts:
            try:
                statuses = self.pubapi.GetUserTimeline(account[0], count=1)
            except Exception, e:
                api = twitter.Api(account[0], account[1])
                statuses = api.GetUserTimeline(account[0], count=1)
            if statuses != []:
                result.append( [str(account[0]), str(statuses[0].text), str(statuses[0].created_at_in_seconds)  ] )
        return result
