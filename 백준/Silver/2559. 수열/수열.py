import sys
input = sys.stdin.readline

def solution(arr, n, k):
    result = []
    result.append(sum(arr[0:k]))
    for i in range(1, n - k + 1):
        result.append(result[i-1] - arr[i-1] + arr[i+k-1])
    return max(result)
    
if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    print(solution(arr, n, k))