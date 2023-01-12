import sys

input = sys.stdin.readline


def main(arr, a, b, c):
    res = 0
    for x in arr:
        if x == 0:
            continue
        if x == 1:
            res += a
        if x == 2:
            res += b * 2
        if x == 3:
            res += c * 3
    return res


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    arr = [0] * 101
    for _ in range(3):
        start, end = map(int, input().split())
        for x in range(start, end):
            arr[x] += 1

    print(main(arr, a, b, c))
    # MAP = [int(inut()) for _ in range(int(input()))]
