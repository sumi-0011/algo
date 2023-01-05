import sys


def main(a, b, c):
    def func(a, b):
        if b == 1:
            return a % c
        elif b == 2:
            return (a * a) % c
        else:
            if b % 2:
                return ((func(a, b // 2) ** 2) * a) % c

            else:
                return (func(a, b // 2) ** 2) % c

    if a % c == 0:
        return 0
    else:
        res = func(a, b)
        return res


if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().split())
    print(main(A, B, C))
