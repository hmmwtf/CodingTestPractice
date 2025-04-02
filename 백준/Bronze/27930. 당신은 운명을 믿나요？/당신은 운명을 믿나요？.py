import sys
input = sys.stdin.readline

word = input().strip()

korea_index = word.find('KOREA')
yonsei_index = word.find('YONSEI')

if korea_index == -1:
    print("YONSEI")
elif yonsei_index == -1:
    print("KOREA")
elif korea_index < yonsei_index:
    print("KOREA")
else:
    print("YONSEI")
