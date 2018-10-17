from requests_futures.sessions import FuturesSession
from concurrent.futures import ThreadPoolExecutor

urls = ['http://speedtest.ftp.otenet.gr/files/test1Mb.db'] * 500

session = FuturesSession(executor=ThreadPoolExecutor(max_workers=100))


def find_multi_reviews(urls):
    resp = [session.get(url).result().status_code for url in urls]
    print(resp)
    return resp


find_multi_reviews(urls)
