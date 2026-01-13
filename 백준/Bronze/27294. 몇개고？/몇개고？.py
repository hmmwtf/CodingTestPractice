t, s = map(int, input().split())

result = 0

if s == 0 and 12 <= t <= 16:
    result = 320
else:
    result = 280

print(result)