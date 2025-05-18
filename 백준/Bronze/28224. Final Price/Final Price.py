import sys

input = sys.stdin.readline

price = []

n = int(input().strip())
for i in range(n):
    price.append(int(input().strip()))

print(sum(price))