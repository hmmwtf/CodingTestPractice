import sys

input = sys.stdin.readline

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

def decimal(n):
    nstr = str(n)
    nl = len(nstr)
    result = 0
    for i in range(nl, 0, -1):
        result += int(nstr[nl - i]) * factorial(i)

    return result

while True:
    n = int(input().strip())
    if n == 0:
        break
    print(decimal(n))
