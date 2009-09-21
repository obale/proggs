#!/bin/bash


#rm -rf *.pot *.po
#xgettext --language=Python --keyword=_ --output=ircbot.pot ircbot.py
#msginit --input=ircbot.pot --locale=en_EN
#msginit --input=ircbot.pot --locale=de_DE

rm -rf en_EN de
mkdir -p en_EN/LC_MESSAGES
mkdir -p de/LC_MESSAGES

msgfmt --output-file=en_EN/LC_MESSAGES/ircbot.mo en_EN.po
msgfmt --output-file=de/LC_MESSAGES/ircbot.mo de.po
