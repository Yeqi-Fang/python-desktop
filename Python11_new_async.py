import asyncio
import time


async def fetch_data():
    print('start')
    await asyncio.sleep(1)
    print('end')
    return 1


async def send_data(name: str):
    print(f'start sending to {name}')
    await asyncio.sleep(2)
    print(f'end sending to {name}')
    return 2


async def main():
    a = await fetch_data()
    b = await asyncio.gather(
        send_data('John'),
        send_data('Sarah'),
        send_data('Jane'),
        send_data('Tom')
    )
    return a, b

if __name__ == '__main__':
    t1 = time.perf_counter()
    a, b = asyncio.run(main())
    print(a, b)
    t2 = time.perf_counter()
    print(t2 - t1)
