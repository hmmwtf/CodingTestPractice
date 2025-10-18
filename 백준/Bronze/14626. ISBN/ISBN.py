import sys

input = sys.stdin.readline

def solution():
    isbn = input().strip()
    total = 0
    isbn_int = [-1] * 13
    for i in range(len(isbn)):
        if '0' <= isbn[i] <= '9':
            isbn_int[i] = int(isbn[i])
    
    for i in range(len(isbn_int)):
        if isbn_int[i] >= 0:
            if i % 2 == 0:
                total += isbn_int[i]
            else:
                total += 3 * isbn_int[i]
    
    answer = 0
    
    for i in range(len(isbn_int)):
        if isbn_int[i] == -1:
            if i % 2 == 0:
                answer = (10 - (total % 10)) % 10
            else:
                answer = (7 * (10 - total % 10)) % 10
    
    print(answer)
    return

if __name__ == "__main__":
    solution()