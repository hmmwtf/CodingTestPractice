import sys
input = sys.stdin.readline 

a,b,c = map(int, input().strip().split())
print((b // a) * c * 3)