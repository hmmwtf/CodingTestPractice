import sys

input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n **(0.5))+1):
        if n % i == 0:
            return 0
    return 1
    
m, n = map(int, input().strip().split())

for i in range(m, n+1):
    if is_prime(i) == 1:
        print(i)