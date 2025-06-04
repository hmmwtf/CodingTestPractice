import sys

input = sys.stdin.readline

a, p = input().strip().split()
seq = []
current = int(a)
seq.append(current)
p = int(p)

while True:
    next_num = sum(int(c)**p for c in str(current))
    
    if next_num in seq:
        print(seq.index(next_num))
        break
    
    seq.append(next_num)
    current = next_num