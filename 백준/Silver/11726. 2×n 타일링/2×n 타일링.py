import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = [1, 2]

    for x in range(2, n):
        res = (dp[x - 2] + dp[x - 1]) % 10007
        dp.append(res)

    print(dp[n - 1])
