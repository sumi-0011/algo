def solution(rsp):
    answer = ''
    
    for x in list(rsp):
        if x == '2':
            answer += '0'
        if x == '0':
            answer += '5'
        if x == '5':
            answer += '2'
    return answer