import sys

while(1):
    line_input = sys.stdin.buffer.readline().decode("utf-8").strip()

    if(line_input == "0"):
        break

    numbers = list(map(int, line_input.split()))

    sys.stdout.write(f'{len(numbers)}\n')

