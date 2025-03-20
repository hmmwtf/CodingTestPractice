k = int(input())

arr = []

for i in range(k):
    val = int(input())
    if val == 0:
        arr.pop()
    else:
        arr.append(val)

print(sum(arr))