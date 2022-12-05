import sys

def fibo(x):
    global dp
    # 탑다운
    # 종료 조건
    if x == 1 or x == 2:
        return 1

    if dp[x] !=0:
        return dp[x]

    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

def fibo_bottom(n):
    # 바텀업
    dp = [0] * 100

    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

if __name__ == "__main__":
    #sys.stdin = open("index.txt", "r")

    n = int(sys.stdin.readline().rstrip())

    dp = [0] * 100

    print(fibo(n))

