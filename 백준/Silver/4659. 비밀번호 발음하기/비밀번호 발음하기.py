import sys
input = sys.stdin.readline

def password(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word_set = set(word)
    
    answer = 0
    
    if vowels & word_set:
        answer += 1
    
    cnt = 0
    vcnt = 0
    second = 0
    for i in range(len(word)):
        if word[i] in vowels:
            vcnt += 1
            cnt = 0
        else:
            cnt += 1
            vcnt = 0
        if cnt == 3 or vcnt == 3:
            second = 1
    
    if second == 0:
        answer += 1

    third = 0
    for i in range(0, len(word) - 1):
        if (word[i] == 'o' and word[i + 1] == 'o') or (word[i] == 'e' and word[i + 1] == 'e'):
            pass
        elif word[i] == word[i + 1]:
            third = 1
            break
    
    if third == 0:
        answer += 1
    
    if answer == 3:
        return True
    else:
        return False
    

if __name__ == "__main__":
    while True:
        word = input().strip()
        if word == "end":
            break
        if password(word):
            print(f"<{word}> is acceptable.")
        else:
            print(f"<{word}> is not acceptable.")