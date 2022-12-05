import sys

MAX = 10 ** 6 + 1

if __name__ == "__main__":
    # sys.stdin = open("index.txt", "r")

    n = int(sys.stdin.readline().rstrip())

    dp = [-1] * MAX

    dp[0] = 0
    dp[1] = 0
    for x in range(2, n+1):
        case1, case2, case3 = MAX, MAX, MAX

        case3 = dp[x - 1] + 1
        if x % 2 == 0:
            case2 = dp[x // 2] + 1
        if x % 3 == 0:
            case1 = dp[x // 3] + 1

        dp[x] = min(case1, case2, case3)

    print(dp[n])