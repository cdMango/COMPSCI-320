import sys

# Citations
# https://www.geeksforgeeks.org/print-all-pairs-in-an-unsorted-array-with-equal-sum/

def process_line(numbers):
    sum_map = {}
    min_sum = None

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            pair_sum = numbers[i] + numbers[j]
            if pair_sum in sum_map:
                if min_sum is None or pair_sum < min_sum:
                    min_sum = pair_sum
                sum_map[pair_sum].append((i, j))
            else:
                sum_map[pair_sum] = [(i, j)]

    if min_sum is None:
        return "None"
    return f"yes: {min_sum}"

while True:
    line_input = sys.stdin.readline().strip()

    if line_input == '0':
        break

    numbers = list(map(int, line_input.split()))

    print(process_line(numbers))