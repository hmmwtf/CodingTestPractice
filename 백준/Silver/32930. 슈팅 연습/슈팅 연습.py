import sys

input = sys.stdin.readline

def solution():
    n, m = map(int, input().strip().split())
    board = []
    new_targets = []
    
    for i in range(n):
        x, y = map(int, input().strip().split())
        board.append((x, y))
        
    for i in range(m):
        x, y = map(int, input().strip().split())
        new_targets.append((x, y))
    
    cur_x, cur_y = 0, 0
    score = 0
    
    for i in range(m):
        max_dist = - 1
        target_idx = -1
        
        for idx, (x, y) in enumerate(board):
            dist = (cur_x - x) ** 2 + (cur_y - y) ** 2
            if dist > max_dist:
                max_dist = dist
                target_idx = idx
        score += max_dist
        cur_x, cur_y = board[target_idx]
        board.pop(target_idx)
        board.append(new_targets[i])

    print(score)
    
if __name__ == "__main__":
    solution()