import sys

input = sys.stdin.readline

n = int(input().strip())

i = 2
while(True):
    if n == 1:
        break
    if n % i == 0:
        print(i)
        n = n / i
    else:
        i += 1
