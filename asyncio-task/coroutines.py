import asyncio

async def nested() -> int:
    return 42

async def main():
    nested()

    print(await nested())

asyncio.run(main())