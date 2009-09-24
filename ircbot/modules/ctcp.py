# -*- coding: UTF-8 -*-
import helper

def sendCommandPRIVMSG(soc, user, command):
    soc.send(bytearray('PRIVMSG ' + user + ' :\x01' + command + '\x01\r\n'))

def sendCommandNOTICE(soc, user, command):
    soc.send(bytearray('NOTICE ' + user + ' :\x01' + command + '\x01\r\n'))

def inqVERSION(soc, user):
    sendCommandPRIVMSG(soc, user, 'VERSION')

def inqUSERINFO(soc, user):
    sendCommandPRIVMSG(soc, user, 'USERINFO')

def inqFINGER(soc, user):
    sendCommandPRIVMSG(soc, user, 'FINGER')

def inqCLIENTINFO(soc, user):
    sendCommandPRIVMSG(soc, user, 'CLIENTINFO')

def inqTIME(soc, user):
    sendCommandPRIVMSG(soc, user, 'TIME')

def inqSOURCE(soc, user):
    sendCommandPRIVMSG(soc, user, 'SOURCE')

def checkCTCP(soc, user, command):
    if ( command == ':\x01VERSION\x01' ):
        sendCommandPRIVMSG(soc, user, 'VERSION :ircbot:v0.01:linux')
    elif ( command == ':\x01USERINFO\x01' ):
        sendCommandPRIVMSG(soc, user, 'USERINFO :I\'m a python bot written from scratch.')
    elif ( command == ':\x01TIME\x01' ):
        sendCommandPRIVMSG(soc, user, 'TIME :' + helper.getTime() )
    else:
        newcommand = command.strip(':\x01')
        sendCommandNOTICE(soc, user, ':\x01ERRMSG ' + newcommand + ' :Query is unknown\x01')
