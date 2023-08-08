def solution(k, tangerine):
    answer = 0
    
    dict = {}
    for x in tangerine:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    list = sorted(dict.values(), reverse=True) 
    
    for x in list:
        k -= x
        answer +=1
        if k <= 0:
            break
    return answer
