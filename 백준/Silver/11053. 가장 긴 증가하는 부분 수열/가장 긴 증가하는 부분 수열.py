import sys
import bisect

input = sys.stdin.readline
n = int(input().strip())
seq = list(map(int, input().split()))

last_seq = []

for x in seq:
    pos = bisect.bisect_left(last_seq, x)
    
    if pos == len(last_seq):
        last_seq.append(x)
    else:
        last_seq[pos] = x
    
print(len(last_seq))