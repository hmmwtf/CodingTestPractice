import sys

input = sys.stdin.readline

n, b = map(str, input().strip().split())

bint = int(b)

answer = 0

for i in range(0, len(n)):
    if '0' <= n[i] <= '9':
        answer += int(n[i]) * (bint ** (len(n)-i-1))
    elif 'A' <= n[i] <= 'Z':
        answer += (ord(n[i]) - 55) * (bint ** (len(n)-i-1))

print(answer)