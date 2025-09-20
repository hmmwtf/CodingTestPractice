import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    board = []
    
    for i in range(n):
        x, y = map(int, input().strip().split())
        board.append([x, y])
    
    min_rss = float('INF')
    best_a, best_b = 0, 0
    
    for i in range(1, 101):
        a = i
        for j in range(1, 101):
            b = j
            cur_rss = 0
            for [x, y] in board:
                cur_rss += (y - (a * x + b)) ** 2
        
            if cur_rss < min_rss:
                min_rss = cur_rss
                best_a, best_b = a, b
            
    print(best_a, best_b)

if __name__ == "__main__":
    solution()