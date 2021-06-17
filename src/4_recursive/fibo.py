# 0, 1, 1, 2, 3, 5, 8, 11, ...

import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

memo = {}
memo[0] = 0
memo[1] = 1


def fib_memo(n):
    if n in memo:
        return memo[n]
    result = fib(n-1) + fib(n-2)
    memo[n] = result
    return result


def print_fib(num, with_memo=False):
    if with_memo:
        print(fib_memo(num))
    else:
        print(fib(num))


def main(num):
    t1 = time.time()
    print_fib(num)
    t2 = time.time()
    print_fib(num, True)
    t3 = time.time()
    print("non memo: {}".format(t2-t1))
    print("with memo: {}".format(t3-t2))

if __name__ == '__main__':
    num = 37
    main(num)

    # メモ化した方が遅くなる。