def solution(s):
    answer = True
    l = len(s)
    cnt = 0
    for i in range(l):
        if '0' <= s[i] <= '9':
            cnt += 1
    
    if cnt == l and (l == 4 or l == 6):
        answer = True
    else:
        answer = False
        
    return answer