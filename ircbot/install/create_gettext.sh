#!/bin/bash

#rm -rf lang/*
#xgettext --language=Python --keyword=_ --output=lang/ircbot.pot main.py modules/*.py
#msginit --input=lang/ircbot.pot --locale=lang/en_EN
#msginit --input=lang/ircbot.pot --locale=lang/de_DE

rm -rf lang/en_EN
mkdir -p lang/en_EN/LC_MESSAGES
mkdir -p lang/de_DE/LC_MESSAGES

msgfmt --output-file=lang/en_EN/LC_MESSAGES/ircbot.mo lang/en_EN.po
msgfmt --output-file=lang/de_DE/LC_MESSAGES/ircbot.mo lang/de_DE.po
