def solution(s):
    answer = ''
    l = len(s)
    mid = int(l/2)
    if l % 2 == 1:
        answer += s[mid]
    else:
        answer += s[mid - 1] + s[mid]
    return answer