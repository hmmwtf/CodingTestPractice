import sys
import math

n, k = map(int, input().strip().split())

print((math.comb(n, k) % 10007)) 