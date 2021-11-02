import asyncio
import time

async def say_after(delay, what) -> None:
    await asyncio.sleep(delay)
    print(what)

async def main() -> None:
    print(f"started at {time.strftime('%X')}")
    
    await say_after(1, 'Hello')
    await say_after(2, 'World')

    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())