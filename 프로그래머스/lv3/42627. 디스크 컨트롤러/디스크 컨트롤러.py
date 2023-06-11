from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    heap = []
    jobs.sort(key = lambda x : x[0] , reverse = True)
    length = len(jobs)
    time = 0
    while jobs or heap:
        while jobs:
            last = jobs.pop()
            if last[0] <= time:
                # 소요시간, 요청된 시점
                heappush(heap,(last[1], last[0]))
            else:
                jobs.append(last)
                break;
        # 작업할 수 있는 작업이 있는 경우
        if heap:
            current, start_time = heappop(heap)
            answer += time - start_time + current
            time += current
            
        # 작업할 수 있는게 없으면, 먼저 요청이 들어온 작업부터 처리
        else:
            time +=1
            
    
    return answer // length