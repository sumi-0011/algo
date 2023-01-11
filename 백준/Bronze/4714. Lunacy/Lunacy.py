import sys

input = sys.stdin.readline


def main(n):
    num = float(n)

    res = round(num * 0.167, 2)
    num = round(num, 2)
    print('Objects weighing {0:0.2f} on Earth will weigh {1:0.2f} on the moon.'.format(num, res))


if __name__ == "__main__":
    while True:
        n = input()
        if float(n) < 0:
            break
        main(n)
    # MAP = [int(inut()) for _ in range(int(input()))]
