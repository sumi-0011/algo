def solution(numbers):
    answer = 0
    
    max_arr = sorted(numbers, reverse=True)
    min_arr = sorted(numbers, reverse=False)
    
    print(max_arr)
    
    m1 = max_arr[0] * max_arr[1]
    m2 = min_arr[0] * min_arr[1]
    
    return max(m1, m2)