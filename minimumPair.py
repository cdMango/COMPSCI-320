import sys

# Citations
# https://www.geeksforgeeks.org/print-all-pairs-in-an-unsorted-array-with-equal-sum/

def process_line(numbers, numbers_size):
    map = {}

    for i in range(numbers_size):
        for j in range(i+1,numbers_size):
            if numbers[i] + numbers[j] in map:
                map[numbers[i] + numbers[j]].append(numbers[i] + numbers[j])
            else:
                map[numbers[i] + numbers[j]] = [numbers[i] + numbers[j]]

    min = None
    for itr in map:
        if len(map[itr]) > 1:
            if min is None or itr < min:
                min = itr

    if min is None:
        return "None"
    return f"yes: {min}"

while True:
    line_input = sys.stdin.readline().strip()

    if line_input == '0':
        break

    numbers = list(map(int, line_input.split()))

    print(process_line(numbers, numbers_size=len(numbers)))
            
