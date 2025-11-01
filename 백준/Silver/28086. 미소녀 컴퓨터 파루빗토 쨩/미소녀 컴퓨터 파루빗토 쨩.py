import sys

input = sys.stdin.readline

def solution():
    formula = input()
    
    a, b = [], []
    op = ''
    
    for i in range(len(formula)):
        text = formula[i]
        if text in ['+', '-', '*', '/']:
            if i > 0 and formula[i-1].isdigit():
                a = formula[:i]
                b = formula[i+1:]
                op = text
                break
    
    a_int = int(a, 8)
    b_int = int(b, 8)
    
    result = 0
    
    if op == '+':
        result = a_int + b_int
    elif op == '-':
        result = a_int - b_int
    elif op == '/':
        if b_int == 0:
            print("invalid")
            return
        else:
            result = a_int // b_int
    else:
        result = a_int * b_int
        
    real_result = 0
    
    if result > 0:
        real_result = oct(result)[2:]
    else:
        real_result = oct(result)[0] + oct(result)[3:]
    
    print(real_result)
    
if __name__ == "__main__":
    solution()