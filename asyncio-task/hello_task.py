import asyncio
import time

async def say_after(delay, what) -> None:
    await asyncio.sleep(delay)
    print(what)

async def main() -> None:
    task_one = asyncio.create_task(
        say_after(1, 'Hello')
    )

    task_two = asyncio.create_task(
        say_after(2, 'World')
    )

    print(f"Start at {time.strftime('%X')}")

    await task_one
    await task_two

    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())
