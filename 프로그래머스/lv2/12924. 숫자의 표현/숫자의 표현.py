def solution(n):
    answer = 0
    
    for start in range(1, n+1):
        s = 0
        for j in range(start, n+1):
            s += j
            if s == n:
                answer +=1
                break
            if s > n:
                break
        
    
    return answer