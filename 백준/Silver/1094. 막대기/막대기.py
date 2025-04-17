import sys
input = sys.stdin.readline

x = int(input().strip())
ans = bin(x).count('1')
print(ans)