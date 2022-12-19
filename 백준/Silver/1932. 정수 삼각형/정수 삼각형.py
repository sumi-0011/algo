import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = []
    for i in range(N):
        t = list(map(int, sys.stdin.readline().split()))
        arr.append(t)
    dp = [[0 for _ in range(i + 1)] for i in range(N)]
    dp[0][0] = arr[0][0]


    def fuc(i, j):
        if 0 < j < i:
            return max(dp[i - 1][j], dp[i - 1][j - 1]) + arr[i][j]
        if j == 0:
            return dp[i - 1][j] + arr[i][j]
        return dp[i - 1][j - 1] + arr[i][j]


    for i in range(1, N):
        for j in range(i + 1):
            dp[i][j] = fuc(i, j)
            # print((i, j), dp[i][j])

    res = max(dp[N - 1])
    print(res)
