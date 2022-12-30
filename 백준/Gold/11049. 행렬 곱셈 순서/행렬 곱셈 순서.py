import sys

INF = 2 ** 31 - 1


def main(N, arr):
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    muti_dp = [[-1 for _ in range(N)] for _ in range(N)]

    def func(start, end):
        if muti_dp[start][end] != -1:
            return dp[start][end], muti_dp[start][end]
        if start == end:
            dp[start][start] = arr[start]
            muti_dp[start][start] = 0
            return dp[start][end], muti_dp[start][end]
        if start + 1 == end:
            N, M, K = arr[start][0], arr[start][1], arr[end][1]
            muti_dp[start][end] = N * M * K
            dp[start][end] = (N, K)
            return dp[start][end], muti_dp[start][end]

        res = (0, 0)
        muti_res = INF
        for i in range(start, end):
            (N, M), t1 = func(start, i)
            (M, K), t2 = func(i + 1, end)
            t = N * M * K + t1 + t2
            # print((start, i), (i + 1, end), t)
            if muti_res > t:
                muti_res = t
                res = (N, K)

        dp[start][end] = res
        muti_dp[start][end] = muti_res
        return dp[start][end], muti_dp[start][end]

    func(0, N - 1)
    print(muti_dp[0][N - 1])


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    arr = []
    for _ in range(N):
        r, c = map(int, sys.stdin.readline().strip().split())
        arr.append((r, c))

    main(N, arr)
