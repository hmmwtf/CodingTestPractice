import sys

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    p, k, m = [], [], []
    evol_cnt = []
    
    for i in range(n):
        pi = input().strip()
        p.append(pi)
        ki, mi = map(int, input().strip().split())
        k.append(ki)
        m.append(mi)

        cnt = 0
        while True:
            if mi <= 0:
                break
            mi -= ki
            if mi >= 0:
                cnt += 1
                mi += 2
        evol_cnt.append(cnt)

    print(sum(evol_cnt))
    max_evol = max(evol_cnt)
    
    max_idx = -1
    for i in range(n):
        if evol_cnt[i] == max_evol:
            max_idx = i
            break
    
    print(p[max_idx])
    
if __name__ == "__main__":
    solution()