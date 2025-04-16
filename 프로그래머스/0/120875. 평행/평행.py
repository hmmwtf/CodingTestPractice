from itertools import combinations

def solution(dots):
    lines = list(combinations(range(4), 2))
    
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if len(set(lines[i]) & set(lines[j])) == 0:
                x1, y1 = dots[lines[i][0]]
                x2, y2 = dots[lines[i][1]]

                x3, y3 = dots[lines[j][0]]
                x4, y4 = dots[lines[j][1]]
                
                if x2 - x1 != 0 and x4 - x3 != 0:
                    g1 = (y2 - y1) / (x2 - x1)
                    g2 = (y4 - y3) / (x4 - x3)
                    
                    if g1 == g2:
                        return 1
                
                elif x2 - x1 == 0 and x4 - x3 == 0:
                    return 1
    return 0