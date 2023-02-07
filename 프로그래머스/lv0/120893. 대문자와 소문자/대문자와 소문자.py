def solution(my_string):
    answer = ''
    
    for x in list(my_string):
        if x == x.upper():
            answer += x.lower()
        else:
            answer += x.upper()
    return answer