def isFalin(word):
    for i in range(len(word) // 2):      # 0부터 문자열 길이의 절반만큼 반복
        if word[i] != word[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
            return False    # 회문이 아님
    return True

def func(str, cnt):
    global n
    
    if(cnt > n): return False
    if isFalin(str): return True
    if str[0] == str[len(str)-1]:
        return func(str[1:-1],cnt)
    else:
        return func(str[1:],cnt+1) or   func(str[:-1],cnt+1)
    
[str, n] =   input().split(' ')
n = int(n)

res = func(str,0)
print(res)



        
    
    
    
    
    
    

