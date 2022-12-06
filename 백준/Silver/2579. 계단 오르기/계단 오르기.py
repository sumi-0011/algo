import sys


if __name__ == "__main__":
    # sys.stdin = open("index.txt", "r")

    n = int(sys.stdin.readline())
    arr = []
    dp = [-1] * (n + 1)

    for _ in range(n):
        ip = int(sys.stdin.readline())
        arr.append(ip)

    if n == 1:
        print(arr[0])
    elif n == 2:
        print(arr[0] + arr[1])
    elif n == 3:
        print(max(arr[0] + arr[2], arr[1] + arr[2]))
    else:
        dp[1] = arr[0]
        dp[2] = arr[0] + arr[1]
        dp[3] = max(arr[0] + arr[2], arr[1] + arr[2])
        dp[4] = max(arr[0] + arr[1] + arr[3], arr[0] + arr[2] + arr[3])

        for x in range(5, n + 1):
            dp[x] = arr[x - 1] + max(dp[x - 2], dp[x - 3] + arr[x - 2])
            # print(x, dp[x])

        print(dp[n])
