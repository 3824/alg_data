## calc GCD(greatest common divisor)
# GCD(m, n) = GCD(n, m%n) ; (m > n)
# ex. 120, 32
# [ 120 = 2^3 * 3 * 5 ]
# [ 32  =  2^3 * 2 ]
# 120 % 32 = 24
# 32 % 24 = 8
# 24 % 8 = 0  => return 8

def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)

if __name__ == '__main__':
    m = 120
    n = 32
    print(gcd(m, n))