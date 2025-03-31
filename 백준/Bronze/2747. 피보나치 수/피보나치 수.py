import sys
input = sys.stdin.readline

def fibo(n):
    num = [0,1]
    if n == 1 or n == 2:
        return 1 
    for i in range(2, n + 1):
        num.append(num[i-1]+num[i-2])
    return num[n]
    
n = int(input().strip())
print(fibo(n))