import sys

input = sys.stdin.readline

n = int(input().strip())
bi = bin(n)[2:][::-1]
answer = 0
for i in range(0, len(bi)):
    if bi[i] == '1':
        answer += 3 ** i

print(answer)