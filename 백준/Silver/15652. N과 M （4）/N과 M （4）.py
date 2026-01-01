import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

def solve():
    n, m = map(int, input().strip().split())
    arr = [i for i in range(1, n + 1)]
    
    for com in combinations_with_replacement(arr, m):
        print(' '.join(map(str,com)))
    
if __name__ == "__main__":
    solve()