def solution(n, lost, reserve):
    answer = 0
    
    arr = [True for i in range(n +1)]
        
    # 도난 체크
    for i in lost:
        arr[i] = False
    
    # 도난 + 여벌 o
    # for i in range(n+1):
        
    newReserve = [False for i in range(n +1)]
    for i in reserve:
        if arr[i]:
            newReserve[i] = True
        arr[i] = True
    
    
    for i in range(1,n+1):
        if not arr[i]:
            if i>1 and newReserve[i-1]:
                arr[i] = True
                newReserve[i-1] = False
            elif i<n and newReserve[i+1]:
                arr[i] = True
                newReserve[i+1] = False
    
    
    
    return arr[1:].count(True)