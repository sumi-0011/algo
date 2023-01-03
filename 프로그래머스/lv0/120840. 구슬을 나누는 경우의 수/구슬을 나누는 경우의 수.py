from itertools import combinations
def factorial(a):
    result = 1
    for item in range(1, a+1, 1):
        result *= item      #result = result * item
    return result
def solution(balls, share):
    answer = 0
    
    nFact = factorial(balls)
    n_mFact = factorial(balls - share)
    mFact = factorial(share)
    
    
    # items = [i for i in range(balls)]
    # res = list(combinations(items, share))
    
    return nFact // (n_mFact * mFact)
    