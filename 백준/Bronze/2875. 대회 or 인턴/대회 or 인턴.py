import sys


def main(N, M, K):
    maxCnt = N // 2

    if maxCnt > M:
        maxCnt = M
    # k 고려
    # if M - maxCnt >= K:
    #     return maxCnt

    for x in range(0, maxCnt):
        cnt = maxCnt - x
        students = (N - cnt * 2) + (M - cnt)
        if students >= K:
            return cnt

    return 0


if __name__ == "__main__":

    N, M, K = map(int, sys.stdin.readline().strip().split())
    res = main(N, M, K)
    print(res)
    # arr = []
    # maxTime = 0
    # for _ in range(N):
    #     r, c = map(int, sys.stdin.readline().strip().split())
    #     arr.append((r, c))
    #     maxTime = max(maxTime, c)
    # main(maxTime, arr)
