import re

def clghks(new_id):
    res = ""
    for x in new_id:
        res += x.lower()
    return res
    
def removeChar(str):
    res =""
    for x in str:
        if "a" <= x <= "z" or "0" <= x <= "9" or x in ['.','-','_']:
            res +=x
    return res

def akclavy_2(str):
    prev = False
    res = ''
    for x in str:
        if x == '.':
            prev = True
        else:
            if prev:
                res+='.'
                prev=False
            res +=x
        
    
    return res

def step4(str):
    if len(str) < 1:
        return str
    
    if  str[0] == '.':
        str = str[1:]
    if  str[-1]== '.':
        str  = str[:-1]
    return str


def step5(str):
    if len(str) ==0:
        return "a"
    return str

def step6(str):
    if len(str) >15:
        str = str[ :15]
        
        if str[-1]== '.':
            str  = str[:-1]
        
    return str
def step7(str):
    while len(str) <= 2:
        str +=str[-1]
        
    return str
def solution(new_id):
    
    answer = clghks(new_id) #1
    answer = removeChar(answer)
    answer = akclavy_2(answer)
    print(answer)
    answer = step4(answer)
    answer = step5(answer)
    answer = step6(answer)
    answer = step7(answer)
    
    return answer   