from collections import deque
def solution(progresses, speeds):
    answer = []
    arr = deque()
    
    for i in range(len(progresses)):
        arr.append(i)
    
    while arr:
        for idx in arr:
            progresses[idx] += speeds[idx]
        cnt = 0
        while len(arr) > 0 and progresses[arr[0]] >= 100:
            arr.popleft()
            cnt +=1
        
        if cnt > 0 :
            answer.append(cnt)
    return answer