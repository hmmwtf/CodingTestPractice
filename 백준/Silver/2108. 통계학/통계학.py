import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().strip())
nums = []
for i in range(n):
    x = int(input().strip())
    nums.append(x)
nums.sort()

am = round(sum(nums) / n)
medium = nums[n//2]
freq = Counter(nums)

max_freq = max(freq.values())
candi_freq = [num for num, count in freq.items() if count == max_freq]
candi_freq.sort()

if len(candi_freq) == 1:
    mode = candi_freq[0]
else:
    mode = candi_freq[1]
    
width = max(nums) - min(nums)

print(am)
print(medium)
print(mode)
print(width)