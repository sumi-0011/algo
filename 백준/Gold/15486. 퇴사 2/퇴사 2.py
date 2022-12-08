import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = []
    dp = [0 for _ in range(n + 1)]
    for i in range(n):
        T, P = map(int, sys.stdin.readline().split(" "))
        arr.append((T, P))

    for i in range(n):
        T, P = arr[i]
        if i + T <= n:
            dp[i + T] = max(dp[i + T], dp[i] + P)
        dp[i + 1] = max(dp[i + 1], dp[i])

    print(max(dp))
