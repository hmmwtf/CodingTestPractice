from itertools import combinations

arr = [] 
for i in range(9):
    arr.append(int(input()))

for num in list(combinations(arr, 7)):
    if sum(num) == 100:
        for shorted in sorted(num):
            print(shorted)
        break