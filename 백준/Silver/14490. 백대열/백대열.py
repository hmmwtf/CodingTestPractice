import sys

input = sys.stdin.readline

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
def solution():
    n, m = map(str, input().strip().split(':'))
    n_int, m_int = int(n), int(m)
    gcd = GCD(n_int, m_int)
    print(f"{int(n_int / gcd)}:{int(m_int / gcd)}")
    
if __name__ == "__main__":
    solution()