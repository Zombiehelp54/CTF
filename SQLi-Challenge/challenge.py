#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading
import time
import  mysql.connector
import urllib.parse

conn = mysql.connector.connect(user='ctf', password = '', host = 'localhost', port = '3306', database = 'ctf')
cursor = conn.cursor()

class Handler(BaseHTTPRequestHandler):
    def setup(self):
        self.timeout=10 # Timeout connections after 10 seconds
        BaseHTTPRequestHandler.setup(self)
    def do_GET(self):
       try:
        self.send_response(200)
        self.send_header("Content-Type", "Text/HTML")
        self.end_headers()
        ip = self.client_address[0]

        if "user" in self.path:
            i_slash = self.path.index('/')
            val = self.path[(i_slash + 6):]
            sql_query(urllib.parse.unquote(val))
            time.sleep(1000) # Never Respond
        else:
            self.wfile.write(b'<b> Welcome to my SQLi challenge </b> <br> This is a simple SQL Injection challenge based on a SQLi vulnerability that I\'ve found while doing bug bounty. <br> To access the challenge: <a target=_blank href=/user/1> Click Here </a> <br> You have to extract the user\'s password from the database. DBMS is mysql <br> <b> PS: The delayed server response is part of the challenge </b><br> DM me with the flag @Zombiehelp54')
       except:
        print("Exception")
    def log_message(self, format, *args):
        return

def sql_query(val):
        val = val.replace(';', '')
        cursor.execute("select name from user where id = %s" % val)
        cursor.fetchall()

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    server = ThreadingSimpleServer(('138.68.169.56', 8900), Handler)
    server.serve_forever()

if __name__ == '__main__':
    run()
