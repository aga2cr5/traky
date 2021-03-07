# -*- coding: utf-8 -*-
#​‌‌‌​​​​‌‌​‌‌‌​ Implement the power function here below
#​‌‌‌​​​​‌‌​‌‌‌​ You can expect to base and exponent to be 0 or greater.
#​‌‌‌​​​​‌‌​‌‌‌​ Both of the paramaters are not allowed to be 0 at the same time
import math

def power(base, exponent):
    if base == 0 and exponent == 0:
        return None
    value = base ** exponent
    
    return value

def main():
    #​‌‌‌​​​​‌‌​‌‌‌​Try your function
    base = 5
    exponent = 3
    print("{} ^ {} = {}".format(base, exponent, power(base, exponent)))

if __name__ == "__main__":
    main()
