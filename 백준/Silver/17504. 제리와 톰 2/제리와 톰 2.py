import sys

input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input().strip())
nums = list(map(int, input().strip().split()))

last_num = nums[-1]
den = 1
for i in range(n-2, -1, -1):
    last_num, den = nums[i] * last_num + den, last_num
gcd = gcd(last_num, den)
print((last_num // gcd) - (den // gcd), last_num // gcd)