import sys

input = sys.stdin.readline

def solution():
    l = int(input().strip())
    word = input().strip()
    
    answer = 0
    
    for i in range(l):
        answer += (ord(word[i]) - ord('a') + 1) * 31 ** i

    print(answer)
    
if __name__ == "__main__":
    solution()