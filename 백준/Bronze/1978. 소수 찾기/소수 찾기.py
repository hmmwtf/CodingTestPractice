def is_prime(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        cnt =  0
        for i in range(2, n+1):
            if n % i == 0:
                cnt += 1
        if cnt == 1:
            return 1
        else:
            return 0

n = int(input())
cnt = 0
arr = list(map(int,input().split()))
for i in arr:
    if is_prime(i) == 1:
        cnt += 1

print(cnt)
    