from requests_futures.sessions import FuturesSession
from concurrent.futures import ThreadPoolExecutor
from time import sleep

urls = ['http://speedtest.ftp.otenet.gr/files/test1Mb.db'] * 50

session = FuturesSession(executor=ThreadPoolExecutor(max_workers=500))

def find_multi_reviews(urls):
    resp = [session.get(url) for url in urls]
    return resp

results = find_multi_reviews(urls)
for i, future in enumerate(results):
	while future.running():
		sleep(.1)
	print(f'future {i} {(future.result().status_code)}')
