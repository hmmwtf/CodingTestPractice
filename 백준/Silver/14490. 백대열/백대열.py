import sys

input = sys.stdin.readline

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
def solution():
    n, m = map(int, input().strip().split(':'))  
    gcd = GCD(n, m)
    print(f"{n // gcd}:{m // gcd}")  
    
if __name__ == "__main__":
    solution()