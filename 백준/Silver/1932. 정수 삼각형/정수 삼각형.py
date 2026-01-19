import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    triangle = []
    
    for i in range(n):
        side = list(map(int, input().strip().split()))
        triangle.append(side)
    
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                triangle[i][j] += triangle[i-1][0] 
            elif j == i:
                triangle[i][j] += triangle[i-1][i-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    print(max(triangle[n -1]))
    
if __name__ == "__main__":
    solve()