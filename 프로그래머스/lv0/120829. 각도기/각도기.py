def solution(angle):
    answer = 0
    
    if angle < 90: return 1
    if angle == 90: return 2
    if angle < 180 : return 3
    return 4
    
    return answer