import sys

input = sys.stdin.readline

def Padovan(n):
    
    if n <= 3:
        return 1
    else:
        arr = [1] * (n + 1)
        for i in range(4, n + 1):
            arr[i] = arr[i - 2] + arr[i - 3]
        return arr[n]

def solve():
    t = int(input().strip())
    
    for i in range(t):
        n = int(input().strip())
        print(Padovan(n))

if __name__ == "__main__":
    solve()