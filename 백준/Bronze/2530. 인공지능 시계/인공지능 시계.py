import sys
input = sys.stdin.readline

a, b, c = map(int, input().strip().split())
time = int(input().strip())

h = time // 3600
m = (time % 3600) // 60
s = time % 60

result_a = a + h
result_b = b + m
result_c = c + s

if result_c >= 60:
    result_c -= 60
    result_b += 1

if result_b >= 60:
    result_b -= 60
    result_a += 1

if result_a >= 24:
    result_a %= 24

print(result_a, result_b, result_c)