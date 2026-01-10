import sys

input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a 
    else:
        return gcd(b, a % b)

def solve():
    n, s = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))

    diff = []

    for i in range(n):
        distance = a[i] - s
        if distance < 0:
            distance = (-1) *distance
        diff.append(distance)
    
    result = diff[0]
    for i in range(1, n):
        result = gcd(result, diff[i])
    
    print(result)
    
if __name__ == "__main__":
    solve()