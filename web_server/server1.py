import datetime
import http.server
import socketserver
import http.client
import pprint

d = []
with open('data.txt', 'r') as f:
    d = f.read().splitlines()

for i in d:
    port = int(d[0])
    file = str(d[1])

if file != "":
    a = file.find('.')
    type_file = file[a + 1:]
else:
    type_file = 'png'

err = ""

if file != "" and type_file != 'png':
    err = 'Error 403'
    file = 'error403.html'
elif file == "":
    err = 'Error 404'
    file = 'error404.html'
else:
    err = "No errors"


class ReqHand(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = file
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler = ReqHand
with socketserver.TCPServer(("", port), handler) as httpd:
    a = ("Date: " + str(datetime.datetime.now()) +
         "\nPort: " + str(port) +
         "\nFile name: " + file +
         "\nErrors: " + str(err))
    print(a)

    httpd.serve_forever()
