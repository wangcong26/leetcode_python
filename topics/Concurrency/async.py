import asyncio

# coroutines

# create a wrapper and return coroutine object
# it doesn't work as usual python function. It needs "await"
# It needs the async event-loop which is a programming construct or design patter that waits for and dispatches events
# or messages in a program (wiki)
async def main():
    print('tim')
    task = asyncio.create_task(foo('text'))
    # await task # wait taks to finish before doing next. If removed, then 'finished' printed first
    await asyncio.sleep(2)
    print('finished')

async def foo(text):
    print(text)
    # in order to run coroutine must use await to execute inside async def
    await asyncio.sleep(1)

asyncio.run(main()) # give a coroutine