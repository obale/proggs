# -*- coding: UTF-8 -*-
import os
import sys
import gettext

def init():
    APP_NAME = "ircbot"
    langs = ["en_EN", "de_DE"]
    local_path = os.path.realpath(os.path.dirname(sys.argv[0])) + '/lang/'
    gettext.bindtextdomain(APP_NAME, local_path)
    gettext.textdomain(APP_NAME)
    init._ = gettext.gettext

def getGettext():
    return init._
