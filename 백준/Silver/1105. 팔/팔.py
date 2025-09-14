import sys
input = sys.stdin.readline

def solution():
    L, R = map(int, input().strip().split())
    
    Lstr = str(L)
    Rstr = str(R)
    
    if len(Lstr) != len(Rstr):
        return 0
    
    cnt = 0
    for i in range(0, len(Lstr)):
        if Lstr[i] == Rstr[i]:
            if Lstr[i] == '8':
                cnt += 1
        else:
            break
    
    return cnt

if __name__ == "__main__":
    print(solution())