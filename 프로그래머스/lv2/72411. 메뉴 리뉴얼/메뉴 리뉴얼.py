from itertools import combinations

# def getMax(cnt, dict):
    
#     sorted_nums = sorted(dict.values(), reverse=True)
    
#     tidx = 0
#     tmax = sorted_nums[tidx]
#     while True:
#         tcnt = 0
#         tmax = sorted_nums[tidx]
#         for v in dict.values():
#             if v >= tmax:
#                 tcnt+=1
#         tidx +=1
        
#         if tcnt >= cnt:
#             break
#     return  tmax
    
def solution(orders, course):
    answer = []
    
    for cours in course:
        dict = {} 
        for order in orders: 
            items = sorted(list(order)) 
            res = list(combinations(items, cours))
            for resC in res:
                resStr = "".join(resC) 
                dict[resStr] = dict[resStr] +1 if resStr in dict else 1
        
        
        tmax = max(dict.values())
        
        if tmax < 2:
            break
            
        for key in dict:
            if dict[key] >= tmax:
                answer.append(key)
    
    return sorted(answer)