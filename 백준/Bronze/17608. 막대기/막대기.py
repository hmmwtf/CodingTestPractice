import sys

input = sys.stdin.readline

n = int(input().strip())
height = [int(input().strip()) for _ in range(n)]

stack = []

stack.append(height[-1])

for i in range(n - 2, -1, -1):
    if height[i] > stack[-1]:
        stack.append(height[i])

print(len(stack))