import sys

# sys.setrecursionlimit(10 ** 6)  # 최대 재귀 설정


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    arr = []

    dp = [-1 for _ in range(N + 2)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2


    def sol(length):
        if dp[length] != -1:
            return dp[length]

        dp[length] = sol(length - 1) + sol(length - 2)

        return dp[length]


    for i in range(3, N + 1):
        sol(i)
    if M == 0:
        print(dp[N])

    else:
        prev = 0
        answer = 1
        for _ in range(M):
            x = int(sys.stdin.readline())
            answer *= dp[x - prev - 1]
            prev = x
        answer *= dp[N - prev]
        print(answer)
