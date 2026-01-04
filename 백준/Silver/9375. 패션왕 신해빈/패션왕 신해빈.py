import sys

input = sys.stdin.readline

def solve():
    t = int(input().strip())
    
    for i in range(t):
        n = int(input().strip())
        clothes = {}
        result = 1
        
        for i in range(n):
            cloth_name, cloth_type = input().strip().split()
            
            if cloth_type in clothes:
                clothes[cloth_type] += 1
            else:
                clothes[cloth_type] = 1
            
        for cnt in clothes.values():
            result *= (cnt + 1)
        print(result - 1)
        
if __name__ == "__main__":
    solve()