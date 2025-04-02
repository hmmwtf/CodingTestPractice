import sys
input = sys.stdin.readline

w = float(input().strip())
h = float(input().strip())
bmi = w / (h ** 2)

if bmi > 25:
    print("Overweight")
elif 18.5 <= bmi <= 25:
    print("Normal weight")
else:
    print("Underweight")