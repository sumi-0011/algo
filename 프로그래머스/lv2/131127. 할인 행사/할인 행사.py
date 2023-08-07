def solution(want, number, discount):
    answer = 0
    
    want_dict = {}
    result_dict = {}
    
    for idx in range(len(want)):
        want_dict[want[idx]] = number[idx]
        result_dict[want[idx]] = 0
    
    for idx in range(len(discount)):
        result_dict[discount[idx]] = 0
        
    def check():
        for key in want:
            if result_dict[key] >= want_dict[key]:
                continue
            return False
        return True
            
            
    result_dict[discount[0]] = 1
    for idx in range(1, len(discount)):
        if check():
            answer +=1
            
        result_dict[discount[idx]] +=1
        if idx >= 10:
            result_dict[discount[idx-10]] -=1
    if check():
        answer +=1
    return answer