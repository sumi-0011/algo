import sys


def main(str):
    print(str[0] + str[-1])


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    for x in range(n):
        str = sys.stdin.readline().strip()
        main(str)
