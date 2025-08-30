import sys
input = sys.stdin.readline

def solution(n: int, m: int, k: int, d: int) -> int:
    inner = n * (m * (m - 1) / 2)
    out = (n * (n - 1) / 2) * (m * m)
    
    base = inner * k + out
    
    bmax = d // base
    if bmax == 0:
        return -1
    else:
        return int(base * bmax)

if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n, m, k, d = map(int, input().strip().split())
        print(solution(n, m, k, d))