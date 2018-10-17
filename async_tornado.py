from tornado import ioloop, httpclient

i = 0
result = []

def handle_request(response):
    result.append(response.code)
    global i
    i -= 1
    if i == 0:
        ioloop.IOLoop.instance().stop()

http_client = httpclient.AsyncHTTPClient()
for i in range(0,500):
    i += 1
    http_client.fetch('http://speedtest.ftp.otenet.gr/files/test1Mb.db', handle_request, method='HEAD')

ioloop.IOLoop.instance().start()

print(result)
