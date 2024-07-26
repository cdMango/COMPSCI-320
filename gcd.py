import sys
from math import gcd
from functools import reduce

def compute_gcd(numbers):
    return reduce(gcd, numbers)

while True:
    line_input = sys.stdin.readline().strip()

    if line_input == '0':
        break

    numbers = list(map(int, line_input.split()))

    if len(numbers) == 1:
        print(f'The gcd of the integers is {numbers[0]}.')
    else:
        the_gcd = compute_gcd(numbers)
        print(f'The gcd of the integers is {the_gcd}.')
