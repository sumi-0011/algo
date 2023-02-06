def solution(my_string, n):
    answer = ''
    for x in list(my_string):
        answer += x * n
    return answer