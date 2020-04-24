import asyncio
from time import sleep

async def nested():
    return 42

async def main():
    task = asyncio.create_task(nested())
    await task
    print(task)
    print(task.result())

asyncio.run(main())
