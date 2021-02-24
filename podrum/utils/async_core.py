from threading import Thread
import sys
import asyncio

class async_core:
    async def ainput(text):
        loop = asyncio.get_event_loop()
        future = loop.create_future()
        def run():
            sys.stdout.writelines(text)
            line = sys.stdin.readline()
            loop.call_soon_threadsafe(future.set_result, line)
        Thread(target = run, daemon = True).start()
        return await future
      
    async def aprint(text):
        loop = asyncio.get_event_loop()
        task = loop.create_task(sys.stdout.writelines(f"{text}\n"))
        await task
