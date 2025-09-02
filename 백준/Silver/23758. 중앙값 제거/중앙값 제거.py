import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    nums.sort()
    cnt = 0
    median_idx = (n + 1) // 2
    
    for x in nums[:median_idx]:
        while x > 1:
            cnt += 1
            x = x // 2
        
    print(cnt + 1)

if __name__ == "__main__":
    solution()