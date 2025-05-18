import sys

input = sys.stdin.readline

L = int(input().strip())
A = int(input().strip())
B = int(input().strip())
C = int(input().strip())
D = int(input().strip())

a, b = 0, 0
if A % C == 0:
    a = A // C
else:
    a = (A // C) + 1
    
if B % D == 0:
    b = B // D
else:
    b = (B // D) + 1

d = max(a, b)

print(L-d)