import asyncio

async def nested() -> int:
    return 42

async def main():
    task = asyncio.create_task(nested())

    await task

asyncio.run(main())