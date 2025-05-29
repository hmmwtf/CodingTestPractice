import sys

input = sys.stdin.readline

n = int(input().strip())

n_copy = n

nums =[]

while n_copy > 0:
    nums.append(n_copy % 10)
    n_copy //= 10

nums.reverse()

cnt = 0
for i in range(1, len(nums)):
    multi1 = 1
    for j in range(0, i):
        multi1 *= nums[j]
    
    multi2 = 1
    for k in range(i, len(nums)):
        multi2 *= nums[k]
    
    if multi1 == multi2:
        cnt += 1

if cnt >= 1:
    print("YES")
else:
    print("NO")
    
        
