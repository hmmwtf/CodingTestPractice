import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    expect_rank = []
    for i in range(n):
        expect_rank.append(int(input().strip()))
    expect_rank.sort()
    
    real_rank = [i for i in range(1, n + 1)]
    
    answer = 0
    for i in range(n):
        answer += abs(real_rank[i] - expect_rank[i])
    
    print(answer)

if __name__ == "__main__":
    solution()