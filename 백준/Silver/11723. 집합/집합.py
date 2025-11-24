import sys

input = sys.stdin.readline

def solution():
    m = int(input().strip())
    s = set()
    for _ in range(m):
        order = list(map(str, input().strip().split()))
        cmd = order[0]
        
        if cmd == "add":
            s.add(int(order[1]))
        elif cmd == "remove":
            s.discard(int(order[1]))
        elif cmd == "check":
            if int(order[1]) in s:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if int(order[1]) in s:
                s.discard(int(order[1]))
            else:
                s.add(int(order[1]))
        elif cmd == "all":
            s = set(range(1, 21))
        elif cmd == "empty":
            s.clear()
        else:
            print("invalid input")

if __name__ == "__main__":
    solution()