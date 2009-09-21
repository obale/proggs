import os, sys
import gettext

APP_NAME = "ircbot"
langs = []
langs += ["en_EN", "de"]
local_path = os.path.realpath(os.path.dirname(sys.argv[0]))
gettext.bindtextdomain(APP_NAME, local_path)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

print _(' my friend. May the force be with you.')
