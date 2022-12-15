import sys

INF = 100000 * 500


def func(start, end):
    global dp, arr, prev_sum
    if start == end:
        return 0

    if dp[start][end]:
        return dp[start][end]

    total = prev_sum[end] - prev_sum[start] + arr[start]
    res = INF
    for i in range(start, end):
        res = min(res, func(start, i) + func(i + 1, end) + total)

    dp[start][end] = res

    return dp[start][end]


if __name__ == "__main__":
    # 파일과 누적합을 따로
    T = int(sys.stdin.readline())
    for _ in range(T):
        K = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split(" ")))

        dp = [[0 for j in range(K)] for i in range(K)]

        prev_sum = []
        prev = 0
        for x in arr:
            prev += x
            prev_sum.append(prev)

        func(0, K - 1)
        print(dp[0][K - 1])
