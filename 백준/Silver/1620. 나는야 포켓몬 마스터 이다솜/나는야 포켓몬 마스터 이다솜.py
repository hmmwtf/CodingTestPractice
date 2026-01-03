import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().strip().split())
    name_to_idx = {}
    idx_to_name = {}
    
    for i in range(1, n + 1):
        name = input().strip()
        idx_to_name[i] = name
        name_to_idx[name] = i
    
    for i in range(m):
        quiz = input().strip()
        if quiz.isdigit():
            print(idx_to_name[int(quiz)])
        else:
            print(name_to_idx[quiz])
    
if __name__ == "__main__":
    solve()