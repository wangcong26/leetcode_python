#https://www.youtube.com/watch?v=Y4Gt3Xjd7G8
#https://learning.oreilly.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_15_01/

import asyncio

async def greeting(name):
    return "Hello " + name

async def hello():
    names = ['Guido', 'Dave', 'Paula']
    for name in names:
        print(await greeting(name))

g = greeting('Guido')
loop = asyncio.get_event_loop()
loop.run_until_complete(g)

h = hello()
h


