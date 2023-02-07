def solution(s1, s2):
    # answer = 0
    # for x in s1:
    #     for y in s2:
    #         if x == y:
    #             answer +=1
    l1 = len(s1)
    l2 = len(s2)
    arr = set(s1+s2)
    
    return l1 + l2 - len(arr)