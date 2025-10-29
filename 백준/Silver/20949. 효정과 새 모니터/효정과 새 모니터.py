import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    ppis = []
    for i in range(n):
        w, h = map(int, input().strip().split())
        ppi = (w ** 2 + h ** 2) ** 0.5
        ppis.append((ppi, -(i+1)))
    
    ppis.sort(reverse=True)
    
    for i in range(n):
        print(abs(ppis[i][1]))

if __name__ == "__main__":
    solution()