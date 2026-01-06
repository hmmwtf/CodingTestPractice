from collections import Counter

def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    
    answer = list(result)[0]
    
    return answer