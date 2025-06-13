import sys
input = sys.stdin.readline

n = int(input().strip())

mod = 1000000
p = 1500000  

n %= p  

a, b = 0, 1
for _ in range(n):
    a, b = b, (a + b) % mod

print(a)