import sys

input = sys.stdin.readline

cnt = 0


def main(n, w, h, l):
    # cnt = 0
    # for i in range(1, len(arr) + 1):
    #     for com in combinations(arr, i):
    #         res = sum(com)
    #         if res == s:
    #             cnt += 1
    a = w // l
    b = h // l
    res = a * b

    return min(n, res)


if __name__ == "__main__":
    n, w, h, l = map(int, input().split())
    # arr = list(map(int, input().split()))

    print(main(n, w, h, l))
