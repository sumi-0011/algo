import sys

def fiboWls(n, fibo):
    res = []
    nn = n
    for fi in fibo:
        res.append(nn // fi)
        nn = nn % fi

    return res


def rightShift(arr):
    arr.pop()
    return arr


def calcKilo(arr, fibo):
    res = 0
    for i in range(len(arr)):
        res += arr[i] * fibo[i + 1]
    return res


def getFiboArr():
    maxFibo = 27  # 317811
    fi = [1, 2]
    for i in range(2, maxFibo):
        fi.append(fi[i - 2] + fi[i - 1])

    return fi


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    kilos = []
    for _ in range(T):
        x = int(sys.stdin.readline())
        kilos.append(x)

    fi = getFiboArr()
    sortFibo = sorted(fi, reverse=True)
    for x in kilos:
        res = rightShift(fiboWls(x, sortFibo))
        print(calcKilo(res, sortFibo))
