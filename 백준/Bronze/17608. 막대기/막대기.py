import sys

input = sys.stdin.readline

n = int(input().strip())

height = []

cnt = 1

for i in range(n):
    height.append(int(input().strip()))

view = height[-1]
for i in range(len(height)-2, -1, -1):
    if height[i] > view:
        cnt += 1
        view = height[i]

print(cnt)