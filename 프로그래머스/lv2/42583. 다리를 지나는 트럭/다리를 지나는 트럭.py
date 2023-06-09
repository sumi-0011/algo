from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    b_que = deque([0 for _ in range(bridge_length)])
    t_que = deque(truck_weights)
    
    time = 0
    total_w = 0
    
    while b_que or t_que:
        time +=1
        
        # 다리 큐에서 하나 뺀다
        b_current = b_que.popleft()
        # 다리 큐에서 뺀 값으로 전체 무게를 업데이트 한다
        total_w -= b_current
        if t_que:
            # 전체 무게 + 첫번째 남은 트럭 무게를 계산해, 남은 트럭이 올라올 수 있는지 확인
            t_current = t_que.popleft()

            # 가능하면 큐에 추가
            if total_w + t_current <= weight:
                b_que.append(t_current)
                total_w += t_current
            # 불가능하면 다리 큐에는 빈값, 남은 트럭은 다시 트럭 튜에 넣음
            else:
                b_que.append(0)
                t_que.appendleft(t_current)
    return time
