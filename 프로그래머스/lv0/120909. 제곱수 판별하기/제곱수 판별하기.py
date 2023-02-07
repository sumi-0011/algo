def solution(n):
    answer = 0
    s = set()
    for x in range(1,10000):
        s.add(x*x)
    if n in s:
        return 1
    return 2
    return answer