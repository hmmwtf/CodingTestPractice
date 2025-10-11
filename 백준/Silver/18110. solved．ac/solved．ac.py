import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.append(int(input().strip()))
    arr.sort()
    scope = int(n * 0.15 + 0.5)
    
    realArr = arr[scope:n-scope]
    answer = 0
    
    if len(realArr) == 0:
        print(answer)
    else:
        answer = int((sum(realArr) / len(realArr)) + 0.5)
        print(answer)

if __name__ == "__main__":
    solution()