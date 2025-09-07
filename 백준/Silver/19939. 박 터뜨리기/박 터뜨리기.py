import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().strip().split())
    
    if n >= (k * (k + 1)) // 2:
        s = (n - k  * (k - 1) // 2) // k
        
        candi = [s + i for i in range(0, k)]
        
        cur_sum = sum(candi)
        remain = n - cur_sum
        
        for i in range(remain):
            candi[k -1 -i] += 1
        
        print(max(candi) - min(candi))
    else:
        print(-1)

if __name__ == "__main__":
    solution()