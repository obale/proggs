import re
import socket
import ssl

def getScroogle(searchterm):
        HOST = 'ssl.scroogle.org'
        PORT = 443
        soc = socket.socket()
        sslsoc = ssl.wrap_socket(soc)

        sslsoc.connect( (HOST, PORT) )
        sslsoc.send('POST /cgi-bin/nbbwssl.cgi?Gw=' + searchterm + '\r\n')
        sslsoc.send('Host: ssl.scroogle.org\r\n\n')

        result0 = sslsoc.recv(1024)
        result1 = result0.lower()
        result = re.findall("http[s]*://[a-zA-Z$-_.+!*'(),?;]*", result1)

        return [ result[1] ]
