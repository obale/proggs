#!/bin/bash
# irc.sh - Trivial IRC client on the base of the BASH
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


server="irc.networld.to"
port="8668"
username="obale"
ircin="/tmp/irc.in"
ircout="/tmp/irc.out"
sleepinterval="0.3"
unset channel

init() {
        trap "echo; echo SGINT: Terminating...; echo; quit 2>/dev/null" SIGINT;
        rm -f $ircin $ircout
        touch $ircin $ircout
}

followinput() {
        tail -f --retry -s $sleepinterval $ircin 2> /dev/null | nc $server $port >> $ircout & inputpid=$!
}

outputserver() {
        tail -f --retry -s $sleepinterval $ircout & outputpid=$!
}

login() {
        echo "PASS networldRocks" >> $ircin
        echo "USER " $username "8 * :" $username >> $ircin
        echo "NICK " $username >> $ircin
}

keepalive() {
        while [ 1 == 1 ]; do
                echo "PONG !" >> $ircin
                sleep 90
        done
}

parseinput() {
        shopt -s nocasematch
        while read line; do
                if [[ ${line:0:3} == "MSG" ]]; then
                        if [[ -n ${channel} ]]; then
                                echo "PRIVMSG " $channel " :" ${line:4} >> $ircin
                        fi
                elif [[ ${line:0:4} == "JOIN" ]]; then
                        channel=${line:4}
                        echo $line >> $ircin
                elif [[ ${line:0:4} == "QUIT" ]]; then
                        quit 2> /dev/null
                else
                        echo $line >> $ircin
                fi
        done
}

quit() {
        kill -9 $keepalivepid
        echo "QUIT" >> $ircin
        sleep 1
        kill -9 $inputpid $outputpid
        rm -rf $ircin
        exit 0
}

init
followinput
login
outputserver
keepalive & keepalivepid=$!
parseinput
