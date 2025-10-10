import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    stack = []
    result = []
    current = 1
    flag = 0
    
    for _ in range(n):
        target = int(input().strip())
        
        while current <= target:
            stack.append(current)
            result.append('+')
            current += 1
        
        if stack[-1] == target:
            stack.pop()
            result.append('-')
        else:
            flag = 1
    
    if flag:
        print("NO")
    else:
        for i in range(len(result)):
            print(result[i])
            
if __name__ == "__main__":
    solution()