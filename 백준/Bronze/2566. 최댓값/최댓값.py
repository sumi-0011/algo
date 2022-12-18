import sys

if __name__ == "__main__":
    tmax = -1
    tidx = (1, 1)
    for i in range(1, 10):
        arr = list(map(int, sys.stdin.readline().split(" ")))
        itmax = max(arr)

        if tmax < itmax:
            tmax = itmax
            j = arr.index(itmax) + 1
            tidx = (i, j)

    print(tmax)
    print(tidx[0], tidx[1])
