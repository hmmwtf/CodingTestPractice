import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    t = int(input().strip())
    for i in range(t):
        a, b, x = map(int, input().strip().split())
        answer = x // gcd(a, b)
        print(answer)
