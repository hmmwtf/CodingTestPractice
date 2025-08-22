import sys
from itertools import combinations
input = sys.stdin.readline

def solution(n, s, nums):
    ans = 0
    
    for r in range(1, n + 1):
        for comb in combinations(nums, r):
            if sum(comb) == s:
                ans += 1

    return ans

if __name__ == '__main__':
    n, s = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    print(solution(n, s, nums))