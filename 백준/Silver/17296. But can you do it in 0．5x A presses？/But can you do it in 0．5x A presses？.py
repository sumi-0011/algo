import math
import sys


def pressButton(arr):
    isPress = False
    res = 0
    for x in arr:
        if isPress:
            x -= 0.5
        res += math.ceil(x)
        if x != 0:
            isPress = True
    return res


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = list(map(float, sys.stdin.readline().split()))

    print(pressButton(arr))
