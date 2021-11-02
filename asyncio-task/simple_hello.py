import asyncio

async def main() -> None:
    print("Hello")
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())