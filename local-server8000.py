#!/usr/bin/env python

#### https://stackoverflow.com/questions/10607621/a-simple-website-with-python-using-simplehttpserver-and-socketserver-how-to-onl

import SimpleHTTPServer
import SocketServer
#import os.path
import sys

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # default routing, change index.html if needed
            self.path = '/index.html'
        elif self.path.startswith('/wiki/index.php?title=Template:Fudan'):
            self.path = self.path.replace('&action=raw&ctype=text/css', ''
                                ).replace('/wiki/index.php?title=Template:Fudan/', '/')
            self.path = self.path.replace('&action=raw&ctype=text/javascript', ''
                                ).replace('/wiki/index.php?title=Template:Fudan/', '/')
        elif self.path.find('/T--Fudan-index') > 0 and self.path.endswith('.svg'):
            self.path = '/' + self.path.split('/')[-1]
        elif self.path.startswith('/Team:Fudan/'):
            self.path = '/' + self.path.split('Team:Fudan')[1] + '.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler

port = 8000
if len(sys.argv) > 1:
    try:
        p = int(sys.argv[1])
        port = p
    except ValueError:
        print 'port value provided must be an integer'

print "serving on port %s " % port
server = SocketServer.TCPServer(('0.0.0.0', port), Handler)
server.serve_forever()
