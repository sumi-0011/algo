def solution(num, total):
    answer = []
    
    for n in range(-num, 100):
        arr = [n+x for x in range(num)]
        temp = sum(arr)
        if temp == total:
            return arr
    return answer