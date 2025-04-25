import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    bits = bin(m)[2:][::-1]  
    
    first = bits.find('1')   
    second = bits.rfind('1')  
    
    if first == second:
        print(first - 1, second - 1)
    else:
        print(first, second)