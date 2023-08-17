def solution(s):
    answer = True
    
    if len(s) != 4 and len(s) != 6:
        return False
    
    if s.isnumeric() :
        return True
    
    return False
