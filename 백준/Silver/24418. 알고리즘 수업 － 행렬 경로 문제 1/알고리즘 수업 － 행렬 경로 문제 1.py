import sys
from math import comb
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input().strip())
    cnt1 = comb(2 * n, n)
    cnt2 = n * n 
    print(cnt1, cnt2)
