import asyncio
import aiohttp
import json

async def request_data(url):
    # use aiohttp.request (as a context manager) to get data from url
    # then return data as str

async def get_reddit_top(subreddit):
    # use request_data coroutine to get reddit top
    # url pattern - f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'
    # then unpack data to json:
    # %reddit_name%: {
    #     %post_title%: {
    #         %score%: int,
    #         %link%: str
    #     },
    #     %post_title%: {
    #         %score%: int,
    #         %link%: str
    #     }
    # }

async def main():
    # use asyncio.gather to get tops for reddits "python", "compsci", "microbork"
    # try to use *args instead of hardcoded function calls
    reddits = {
        "python",
        "compsci",
        "microbork"
    }

asyncio.run(main())
