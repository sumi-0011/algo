import sys

N_MAX = 13

if __name__ == "__main__":
    # sys.stdin = open("index.txt", "r")

    T = int(sys.stdin.readline().rstrip())

    dp = [0,1,2,4]

    for x in range(4, N_MAX):
        dp.append(dp[x-1]+ dp[x-2]+ dp[x-3])

    for _ in range(T):
        n = int(sys.stdin.readline().rstrip())
        print(dp[n])





