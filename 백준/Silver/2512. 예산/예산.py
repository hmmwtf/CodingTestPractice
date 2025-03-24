import sys

input = sys.stdin.readline

n = int(input().strip())
budgets = list(map(int, input().strip().split()))
total = int(input().strip())
max_budget = 0
if sum(budgets) <= total:
    max_budget = max(budgets)
else:
    budgets.sort()
    current_budget = 0
    max_budget = 0
    for i in range(n):
        if current_budget + budgets[i] * (n - i) > total:
            max_budget = (total - current_budget) // (n - i)
            break
        current_budget += budgets[i]
        max_budget =budgets[i]
            
print(max_budget)