import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    trees = list(map(int, input().strip().split()))
    trees.sort(reverse=True)
    
    time = []
    
    for i in range(1 , n + 1):
        time.append(i + trees[i-1])

    print(max(time) + 1)

if __name__ == "__main__":
    solution()