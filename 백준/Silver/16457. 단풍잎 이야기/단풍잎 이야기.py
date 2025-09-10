# boj 16457 단풍잎 이야기
import sys
from itertools import combinations
input = sys.stdin.readline

def solution():
    n, m, k = map(int, input().strip().split())
    
    candi = [i for i in range(1, 2 * n + 1)]
    all_skill = []
    for i in range(m):
        skills = list(map(int, input().strip().split()))
        all_skill.append((skills))

    result = []
    cnt = 0
    for comb in combinations(candi, n):
        for i in range(len(all_skill)):
            if all(skill in comb for skill in all_skill[i]):
                cnt += 1
        result.append(cnt)
        cnt = 0
    print(max(result))

if __name__ == "__main__":
    solution()