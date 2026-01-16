import sys

input = sys.stdin.readline

def solve():
    n, k = map(int, input().strip().split())
    lan = []
    for i in range(n):
        lan.append(int(input().strip()))
    
    left = 1
    right = max(lan)
    
    while left <= right:
        mid = (left + right) // 2
        
        count = 0
        for l in lan:
            count += l // mid
        
        if count >= k:
            left = mid + 1
        else:
            right = mid - 1
            
    print(right)
    
if __name__ == "__main__":
    solve()