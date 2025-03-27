import sys
input = sys.stdin.readline

t = int(input().strip())
for i in range(t):
    a, b = map(int, input().strip().split())
    if pow(a, b, 10) == 0:
        print("10")
    else:
        print(pow(a, b, 10))