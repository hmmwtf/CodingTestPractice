import sys
from itertools import permutations

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    k = int(input().strip())
    
    nums = []
    for i in range(n):
        nums.append(int(input().strip()))
    
    result = []
    for per in permutations(nums, k):
        candi = ""
        for i in per:
            candi += str(i)
        result.append(int(candi))
    print(len(set(result)))
    
if __name__ == "__main__":
    solution()