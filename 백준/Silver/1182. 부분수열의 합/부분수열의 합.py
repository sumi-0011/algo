import sys
from itertools import combinations

input = sys.stdin.readline

cnt = 0


def main(arr, s):
    preSum = [arr[0]]
    for i in range(1, len(arr)):
        preSum.append(preSum[i - 1] + arr[i])

    cnt = 0

    for i in range(1, len(arr) + 1):
        combi = combinations(arr, i)
        for com in combi:
            res = sum(com)
            if res == s:
                cnt += 1
    return cnt


if __name__ == "__main__":
    n, s = map(int, input().split())

    arr = list(map(int, input().split()))

    print(main(arr, s))
