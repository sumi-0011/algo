import sys



if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = []
    arr_x = []
    arr_y = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        arr.append((x, y))
        arr_x.append(x)
        arr_y.append(y)

    arr_x.sort()
    arr_y.sort()

    m_x = arr_x[N // 2]
    m_y = arr_y[N // 2]

    res = 0
    for x, y in arr:
        dis = abs(x - m_x) + abs(y - m_y)
        res += dis
    print(res)
