from fractions import Fraction
# 첫번째 인자에 분자, 두번째 인자에 분모
def solution(numer1, denom1, numer2, denom2):
    answer = []
    bottom = denom1 * denom2
    top = numer1 * denom2 + numer2 * denom1
    
    res = Fraction(top,bottom)
    return [res.numerator,res.denominator]
