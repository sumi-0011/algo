import sys
sys.setrecursionlimit(10**6)


def range_check(arr, i, j):
    if 0 <= i < len(arr) and 0 <= j < len(arr[0]):
        return True
    return False


def moving(i, j):
    global res, arr
    if res[i][j] > -1:
        return res[i][j]
    current = arr[i][j]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    result = 0
    for dx, dy in direction:
        x = i + dx
        y = j + dy
        if range_check(res, x, y) and current < arr[x][y]:  # 더 높은 계단
            result += moving(x, y)

    res[i][j] = result
    return res[i][j]


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split(" "))
    arr = []
    for _ in range(M):
        tarr = list(map(int, sys.stdin.readline().split(" ")))
        arr.append(tarr)

    res = [[-1 for j in range(N)] for i in range(M)]
    res[0][0] = 1
    moving(M - 1, N - 1)
    print(res[M - 1][N - 1])
