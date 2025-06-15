import sys

input = sys.stdin.readline

x = input().strip()

answer = 0
if x[0] == '0' and x[1] == 'x':
    for i in range(2, len(x)):
        if 'a' <= x[i] <= 'z':
            answer += int(ord(x[i]) - ord("a") + 10) * (16 ** (len(x) - 1 - i))
        else:
            answer += int(x[i]) * (16 ** (len(x) - 1 - i))
elif x[0] == '0':
    for i in range(1, len(x)):
        answer += int(x[i]) * (8 ** (len(x) - 1 - i))
else:
    answer = int(x)
    
print(answer)
