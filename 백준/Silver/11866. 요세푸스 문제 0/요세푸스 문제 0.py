import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())

seat = []

for i in range(n):
    seat.append(i+1)
    
result = []

idx = 0

while True:
    idx = (idx + k - 1) % len(seat)
    result.append(seat.pop(idx))
    if len(seat) == 0:
        break
    
print("<" + ", ".join(map(str, result)) + ">")