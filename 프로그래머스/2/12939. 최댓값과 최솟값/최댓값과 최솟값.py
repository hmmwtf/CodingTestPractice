def solution(s):
    answer = ''
    arr = s.split()
    arrint = []
    for i in range(len(arr)):
        arrint.append(int(arr[i]))
    x = str(max(arrint))
    y = str(min(arrint))
    return y+' '+x