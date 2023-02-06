def solution(lines):
    answer = 0
    
    lines.sort(key=lambda x : x[0])
    start = -100
    end = -100
    
    dict = {}
    for current_start,current_end in lines:
        if start <= current_start <= end:
            if current_end >= end:
                # 이어져 있고 end 연장
                for n in range(current_start, end):
                    dict[n] = 1
                end = current_end
                
                continue
            # 이어져 있는데 안에 있음 
            for n in range(current_start, current_end):
                    dict[n] = 1
            continue
        # 끊어져있음 end < current start
        if end < current_start:
            start = current_start
            end = current_end
            
    print(dict)
    for x in dict:
        answer+=1
    return answer