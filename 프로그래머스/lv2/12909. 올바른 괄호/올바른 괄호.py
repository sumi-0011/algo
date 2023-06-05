
def solution(s):
    answer = True
    arr = []
    for x in list(s):
        if x == '(':
            arr.append(x)
        if x == ')':
            if len(arr) <= 0:
                return False
            arr.pop()
    if len(arr) == 0:
        return True
    else:
        return False
    

    return True