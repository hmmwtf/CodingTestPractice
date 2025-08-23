import sys
input = sys.stdin.readline

def solution():
    n = int(input().strip())
    nums = [list(map(int, input().strip())) for _ in range(n)]
    
    l = len(nums[0])
    
    for k in range(1, l+1):
        parts = []
        for num in nums:
            part = ''.join(map(str, num[-k:]))
            parts.append(part)
        
        if len(set(parts)) == n:
            print(k)
            return
    
    print(l)

if __name__ == '__main__':
    solution()