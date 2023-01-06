import sys


def main(n):
    arr = [0 for i in range(10)]

    for x in list(str(n)):
        arr[int(x)] += 1

    t69 = arr[6] + arr[9]
    arr[6] = t69 // 2
    arr[9] = t69 - arr[6]

    return max(arr)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(main(n))
