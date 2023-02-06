def solution(array):
    answer = 0
    dict = {}
    for x in array:
        if x in dict:
            dict[x] +=1
        else:
            dict[x] = 1
            
    maxCnt = -1
    for key in dict:
        maxCnt = max(dict[key],maxCnt)
    
    answer = -1
    for key in dict:
        if dict[key] ==maxCnt:
            if answer != -1:
                return -1
            answer = key
    
    return answer