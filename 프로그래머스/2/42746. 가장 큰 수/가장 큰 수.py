def solution(numbers):
    str_nums = list(map(str, numbers))
    str_nums.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(str_nums)
    
    return '0' if answer[0] == '0' else answer