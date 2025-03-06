def solution(n):
    fn = [0 for i in range(n+1)]
    fn[1] = 1
    for i in range(2, n+1):
        fn[i] = fn[i-1] + fn[i-2]
    return fn[n] % 1234567