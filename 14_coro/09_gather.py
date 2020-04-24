import asyncio
from time import sleep, strftime

async def a_count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

def count():
    print("One")
    sleep(1)
    print("Two")

def main():
    for i in range(3):
        count()

async def a_main():
    await asyncio.gather(a_count(), a_count(), a_count())

if __name__ == "__main__":
    print(f"{strftime('%X')}")
    asyncio.run(a_main())
    print(f"{strftime('%X')}")

    print("-"*20)

    print(f"{strftime('%X')}")
    main()
    print(f"{strftime('%X')}")
