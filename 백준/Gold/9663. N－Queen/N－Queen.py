n = int(input())

queen = [-1] * n

def is_able_attack(row, col):
    for i in range(row):
        if queen[i] == col:
            return False
        if abs(row - i) == abs(col- queen[i]):
            return False
    return True

def recursion(n, row):
    count = 0
    if row == n:
        return 1

    for col in range(n):
        if is_able_attack(row, col):
            queen[row] = col
            count += recursion(n, row+1)
    return count

print(recursion(n, 0))