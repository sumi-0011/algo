

def solution(n):
    answer = 0
    
    dp = [0,1]
    for i in range(2, n+1):
        current = (dp[i-1] + dp[i-2]) % 1234567
        dp.append(current) 
    
    
    return dp[n]