import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    encrypted = input().strip()
    original = input().strip()
    
    original_len = len(original)
    encrypted_len = len(encrypted)
    
    if encrypted_len < original_len:
        print("NO")
        continue
    
    original_count = {}
    for char in original:
        original_count[char] = original_count.get(char, 0) + 1
    
    window_count = {}
    
    for i in range(original_len):
        char = encrypted[i]
        window_count[char] = window_count.get(char, 0) + 1
    
    if window_count == original_count:
        print("YES")
        continue
    
    found = False
    for i in range(original_len, encrypted_len):
        remove_char = encrypted[i - original_len]
        add_char = encrypted[i]
        
        window_count[remove_char] -= 1
        if window_count[remove_char] == 0:
            del window_count[remove_char]
        
        window_count[add_char] = window_count.get(add_char, 0) + 1
        
        if window_count == original_count:
            found = True
            break
    
    print("YES" if found else "NO")
