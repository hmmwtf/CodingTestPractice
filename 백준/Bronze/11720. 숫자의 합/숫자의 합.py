import sys

input = sys.stdin.readline

n = int(input().strip())
nums = input().strip()

answer = 0 
for i in range(len(nums)):
    answer += int(nums[i])

print(answer)