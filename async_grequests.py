import grequests

num = 50
urls = ['http://speedtest.ftp.otenet.gr/files/test1Mb.db'] * num

rs = (grequests.get(u) for u in urls)

print(grequests.map(rs))
