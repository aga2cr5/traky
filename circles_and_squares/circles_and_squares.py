# -*- coding: utf-8 -*-
#​‌‌‌​​​​‌‌​‌‌‌​ Implement the count_circles_and_squares function here below

import math

def count_circles_and_squares(length, circles, squares):
    if length < 1.0:
        return circles, squares
    circles += 1

    new_length = (math.sqrt(2) * length) / 2

    if new_length <= 1.0:
        return circles, squares
    squares += 1

    return count_circles_and_squares(new_length, circles, squares)


def main():
    length = 1.5
    circles, squares = count_circles_and_squares(length, 0, 0)
    print("Circles:", circles, "Squares:", squares)


if __name__ == "__main__":
    main()
