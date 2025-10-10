import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    sizes = list(map(int, input().strip().split()))
    t, p = map(int, input().strip().split())
    
    tshirt_bundles = 0
    for size in sizes:
        tshirt_bundles += size // t if size % t == 0 else size // t + 1

    pen_bundles = n // p
    pen_singles = n % p
    
    print(tshirt_bundles)
    print(pen_bundles, pen_singles)
    
if __name__ == "__main__":
    solution()