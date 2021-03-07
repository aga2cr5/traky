# -*- coding: utf-8 -*-
#​‌‌‌​​​​‌‌​‌‌‌​ Implement the sieve_of_eratosthenes function here below
import math

def sieve_of_eratosthenes(n):
    """ Return the number of prime numbers between the range (2, n) """
    if n < 0:
        return 0

    elif n < 2:
        return -1

    else:
        luvut = list(range(2, n + 1))
        print(luvut)
        maara = 0

        for i in range(2, int(math.sqrt(n)) + 1):
            if i != 0:
                j = i * i
                while j <= n:
                    if j in luvut:
                        luvut.remove(j)
                    j = j + i

        for i in luvut:
            if i != 0:
                maara += 1
        print(luvut)

        return maara
'''
4, 6, 8, 9, 10
'''
#​‌‌‌​​​​‌‌​‌‌‌​ Driver program
def main():
    n = 50
    nof_primes = sieve_of_eratosthenes(n)
    print("The number of primes between the range (2, {:d}) is {:d}:".format(n, nof_primes))

if __name__ == "__main__":
    main()
