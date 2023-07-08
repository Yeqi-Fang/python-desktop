import asyncio
import time


async def fetch_data():
    print('start')
    await asyncio.sleep(1)
    print('end')


async def send_data(name: str):
    print(f'start sending to {name}')
    await asyncio.sleep(2)
    print(f'end sending to {name}')


async def main():
    await fetch_data()
    await asyncio.gather(
        send_data('John'),
        send_data('Sarah'),
        send_data('Jane'),
        send_data('Tom')
    )


if __name__ == '__main__':
    t1 = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter()
    print(t2 - t1)
