def solution(my_string, letter):
    answer = ''
    for x in my_string:
        if x != letter:
            answer +=x
    return answer