import sys

input = sys.stdin.readline

def solution():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        feed = list(map(int, input().strip().split()))
        print(solve(n, feed))

def solve(n: int, feed: list[int]) -> int:
    
    day = 1
    
    while True:
        if sum(feed) > n:
            break
        
        new_feed = []
        for i in range(len(feed)):
            new_feed.append(feed[i] + feed[(i-1) % len(feed)] + feed[(i+1) % len(feed)] + feed[(i + int(len(feed) / 2)) % len(feed)])
        feed = new_feed
        day += 1
        
    return day

if __name__ == "__main__":
    solution()