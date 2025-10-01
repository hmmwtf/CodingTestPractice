import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    nstr = str(fact(n))
    cnt = 0
    
    for i in range(len(nstr) - 1, - 1, -1):
        if nstr[i] == '0':
            cnt += 1
        else:
            break
        
    print(cnt)

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n - 1)

if __name__ == "__main__":
    solution()