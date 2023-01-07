import sys


def main(arr):
    papar = [[0 for _ in range(101)] for _ in range(101)]

    for a, b in arr:
        for x in range(a, a + 10):
            for y in range(b, b + 10):
                papar[x][y] += 1
    res = 0
    for ar in papar:
        for x in ar:
            if x:
                res += 1
    return res


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        arr.append((a, b))
    print(main(arr))
