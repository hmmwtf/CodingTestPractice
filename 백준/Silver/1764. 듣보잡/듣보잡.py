import sys

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    
    nolisten = set(input().strip() for _ in range(n))
    nosee = set(input().strip() for _ in range(m))
    
    result = sorted(nolisten & nosee)
    
    print(len(result))
    print('\n'.join(result))

if __name__ == "__main__":
    solution()
