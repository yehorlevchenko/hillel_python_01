def what_is_coro(start_v):
    print(f"Coroutine initiated with {start_v}")
    value = 2 * (yield)
    print(f"New value x2 = {value}")
    value = 3 * (yield)
    print(f"New value x3 = {value}")

c = what_is_coro(2)
next(c)
c.send(2)
c.send(2)
c.close()
