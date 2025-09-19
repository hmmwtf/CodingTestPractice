import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    ans = 0
    min_prime = 0 
    
    for i in range(2, int(n ** 0.5) + 1, 1):
        if n % i == 0:
            min_prime = i
            break
    
    
    if min_prime != 0:
        ans = n - (n / min_prime)
    else:
        ans = n - 1
    
    print(int(ans)) 
    
if __name__ == "__main__":
    solution()