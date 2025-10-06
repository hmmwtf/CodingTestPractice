import sys

data = sys.stdin.read().split()
n = int(data[0])

numbers = []
for i in range(1, n + 1):
    numbers.append(int(data[i][::-1]))

numbers.sort()
print('\n'.join(map(str, numbers)))