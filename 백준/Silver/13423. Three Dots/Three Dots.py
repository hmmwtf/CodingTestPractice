import sys
import bisect
input = sys.stdin.readline

def solution():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        dots = list(map(int, input().strip().split()))
        print(solve(dots))
    return

def solve(dots):
    cnt = 0
    dots.sort()
    
    for b_idx in range(1, len(dots) - 1):
        b = dots[b_idx]
        
        start = 0
        end = len(dots) - 1
        
        while start < b_idx and end > b_idx:
            sum_val = dots[start] + dots[end]
            target = 2 * b
            
            if sum_val == target:
                cnt += 1
                start += 1
                end -= 1
            elif sum_val < target:
                start += 1
            else:
                end -= 1
            
    return cnt

if __name__ == "__main__":
    solution()