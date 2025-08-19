import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().strip().split())

words = [list(input().strip()) for _ in range(n)]

def hammingdistance(seq1, seq2):
    distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance

answer = ''

for i in range(m):
    candi = []
    for j in range(n):
        candi.append(words[j][i])
    cnt = Counter(candi)
    
    max_cnt = max(cnt.values())
    
    result = []
    for nu, count in cnt.items():
        if count == max_cnt:
            result.append(nu)
    
    result.sort()
    answer += result[0]

total_distance = 0
for j in range(n):
    total_distance += hammingdistance(answer, words[j])

print(answer)
print(total_distance)