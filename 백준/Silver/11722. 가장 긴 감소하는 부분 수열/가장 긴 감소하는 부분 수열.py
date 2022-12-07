import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split(" ")))

    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] < arr[j]:  # j i 순으로 즈악
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
