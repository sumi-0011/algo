def solution(sizes):
    answer = 0
    
    first = 0 
    second = 0
    for x, y in sizes:
        ma, mi = max([x,y]), min([x,y])
        if ma > first:
            first = ma
        if mi > second:
            second = mi
            
        # a_x.append(x)
        # a_y.append(y)
        
    
    return first * second