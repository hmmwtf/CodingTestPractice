import sys

input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def solution():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    x = int(input().strip())
    coprime = []
    
    for i in range(n):
        if gcd(a[i], x) == 1:
            coprime.append(a[i])
    
    answer = sum(coprime) / len(coprime)
    print(answer)
    
if __name__ == "__main__":
    solution()