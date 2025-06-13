import sys

input = sys.stdin.readline

n = int(input().strip())

nums = list(map(int, input().strip().split()))

left = [0] * n
right = [0] * n

left[0] = nums[0]
for i in range(1, n):
    left[i] = max(nums[i], left[i-1] + nums[i])

right[-1] = nums[-1]
for i in range(n-2, -1, -1):
    right[i] = max(nums[i], right[i+1] + nums[i])
    
ans = max(left)

for i in range(1, n-1):
    ans = max(ans , left[i-1] + right[i+1])
    
print(ans)