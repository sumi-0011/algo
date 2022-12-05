import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    dp = [1,2,4]

    for x in range(4, 11):
        dp.append(sum(dp[-3:]))

    for _ in range(T):
        n = int(sys.stdin.readline())
        print(dp[n-1])




