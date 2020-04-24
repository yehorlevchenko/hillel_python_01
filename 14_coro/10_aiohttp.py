import aiohttp
import asyncio
from random import randint

urls = [
    "http://ukr.net",
    "http://google.com",
    "http://nv.ua",
    "http://serpstat.com"
]

async def areq(u):
    print(f'a req {u}')
    await asyncio.sleep(randint(1,2))
    async with aiohttp.request('GET', u) as resp:
        print(f'a res {u} - {resp.status}')

async def main():
    await asyncio.gather(*(areq(u) for u in urls))


asyncio.run(main())
