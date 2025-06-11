import sys

input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

a.sort()
b.sort(reverse=True)

answer = 0

for i in range(n):
    answer += a[i] * b[i]

print(answer)