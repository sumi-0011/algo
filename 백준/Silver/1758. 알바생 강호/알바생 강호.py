import sys

input = sys.stdin.readline


def main(arr):
    arr.sort(reverse=True)
    res = 0
    for i in range(len(arr)):
        t = arr[i] - i
        res += t if t >= 0 else 0
    return res


if __name__ == "__main__":
    MAP = [int(input()) for _ in range(int(input()))]
    print(main(MAP))
