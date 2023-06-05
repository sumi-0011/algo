from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque()
    for i in range(len(priorities)):
        que.append((priorities[i], i))
        
    while que:
        max_num, i = max(que)
        current, idx = que.popleft()
        if max_num > current:
            que.append((current, idx))
            continue
            
        answer +=1
        if location == idx:
            return answer
        # if answer > 2:
        #     return;
    return answer