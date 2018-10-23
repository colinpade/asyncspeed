import asyncio
import aiohttp

loop = asyncio.get_event_loop()

async def hello(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            #response = await response.read()

tasks = []

url = "http://speedtest.ftp.otenet.gr/files/test1Mb.db"
for i in range(50):
    task = asyncio.ensure_future(hello(url))
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
