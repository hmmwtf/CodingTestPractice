import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split()))
m = int(input().strip())
b = list(map(int, input().strip().split()))

nodupA = set(a)

for x in b:
    if x in nodupA:
        print(1)
    else:
        print(0)