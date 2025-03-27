import sys
input = sys.stdin.readline

word = input().strip()  # 원본 문자열
bomb = input().strip()  # 폭발 문자열
bomb_len = len(bomb)    # 폭발 문자열

stack = []

for ch in word:
    stack.append(ch)
    
    if len(stack) >= bomb_len and "".join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()
            
result = "".join(stack)

if result == "":
    print("FRULA")
else:
    print(result)