import sys
input = sys.stdin.readline

def count_ops(a, X):
    return sum(ai - X for ai in a if ai > X)

def main():
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    
    low, high = 0, max(a)
    answer = high
    
    while low <= high:
        mid = (low + high) // 2
        if count_ops(a, mid) <= k:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(answer)
    
if __name__ == "__main__":
    main()