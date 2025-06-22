import sys

input = sys.stdin.readline

A, I = map(int, input().strip().split())
print(A * (I - 1) + 1)