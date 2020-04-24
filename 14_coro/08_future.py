import asyncio
import time

async def set_after(fut, delay, value):
    await asyncio.sleep(delay)
    fut.set_result(value)

async def main():
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut1 = loop.create_future()
    fut2 = loop.create_future()
    fut3 = loop.create_future()


    # Run "set_after()" coroutine in a parallel Task.
    loop.create_task(
        set_after(fut1, 2, '... world 1'))
    loop.create_task(
        set_after(fut2, 3, '... world 2'))
    loop.create_task(
        set_after(fut3, 1, '... world 3'))

    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    print(f"{time.strftime('%X')}")
    print(await fut1)
    print(f"{time.strftime('%X')}")
    print(await fut2)
    print(f"{time.strftime('%X')}")
    print(await fut3)
    print(f"{time.strftime('%X')}")

asyncio.run(main())
