import math
def solution(price):
    answer = 0
    
    if price >= 500000:
        return math.floor(price * 0.8)
    if price >= 300000:
        return math.floor(price * 0.9)
    if price >= 100000:
        return math.floor(price  * 0.95)
    
    
    return price