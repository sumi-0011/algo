def solution(n):
    answer = 0
    for x in list(str(n)):
        answer += int(x)
    return answer