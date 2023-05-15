import asyncio
import random


async def worker(name, queue):
    while True:
        n = await queue.get()

        await asyncio.sleep(n / 100)

        result = 0

        for i in range(n):
            result += i

        queue.task_done()

        print(f'[{name}] for {n} got result {result}')


async def main():
    queue = asyncio.Queue()

    tasks = []

    for i in range(100):
        queue.put_nowait(random.randint(i, i * 25))

    for i in range(4):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    await queue.join()

    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())
