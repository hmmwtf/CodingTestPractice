import sys

input = sys.stdin.readline

n = int(input().strip())

points = [list(map(int, input().strip().split())) for _ in range(n)]

points.sort()

def calc_dist(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

def minlen(start, end):
    if end - start <= 2:  
        min_dist = float('inf')
        for i in range(start, end):
            for j in range(i+1, end+1):
                min_dist = min(min_dist, calc_dist(points[i], points[j]))
        return min_dist

    mid = (start + end) // 2
    x_mid = points[mid][0]
    d = min(minlen(start, mid), minlen(mid+1, end))

    strip = []
    for i in range(start, end+1):
        if (points[i][0] - x_mid) ** 2 < d:
            strip.append(points[i])
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) ** 2 >= d:
                break
            d = min(d, calc_dist(strip[i], strip[j]))
    return d

print(minlen(0, n-1))