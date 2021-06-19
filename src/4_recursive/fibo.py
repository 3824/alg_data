# 0, 1, 1, 2, 3, 5, 8, 11, ...

import time
import asyncio


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


memo: dict[int: int] = {}
memo[0] = 0
memo[1] = 1


def fib_memo(n):
    if n in memo.keys():
        return memo[n]
    result = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = result
    return result


def print_fib(num, with_memo=False):
    if with_memo:
        print(fib_memo(num))
    else:
        print(fib(num))


async def main(num):
    timeout_sec = 3
    t1 = time.time()
    is_timeout = False
    try:
        loop = asyncio.get_running_loop()
        await asyncio.wait_for(
            loop.run_in_executor(None, print_fib, num),
            timeout=timeout_sec
        )
    except asyncio.TimeoutError:
        is_timeout = True
    t2 = time.time()
    if is_timeout:
        print("non memo is timeout {}sec".format(timeout_sec))
    else:
        print("non memo: {}sec".format(t2 - t1))
    print_fib(num, True)
    t3 = time.time()
    print("with memo: {}sec".format(t3 - t2))


if __name__ == '__main__':
    num = 50
    asyncio.run(main(num))