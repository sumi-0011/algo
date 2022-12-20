import sys

# sys.setrecursionlimit(10 ** 6)  # 최대 재귀 설정
# INF = 100000 * 500

PASS = 1
FAIL = 0
UNKNOWN = -1

if __name__ == "__main__":

    a, b, c = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())
    arr = []

    dict = [-1 for _ in range(a + b + c + 1)]

    for _ in range(N):
        i, j, k, r = map(int, sys.stdin.readline().split())
        arr.append((i, j, k, r))

        if r == 1:
            dict[i] = PASS
            dict[j] = PASS
            dict[k] = PASS

    # p p p -> s
    # p p u -> f
    # p u u
    # u u u
    for i, j, k, r in arr:
        if r == 1:
            continue
        idx = dict[i] + dict[j] + dict[k]
        if idx == 1:
            if dict[i] == -1: dict[i] = FAIL
            if dict[j] == -1: dict[j] = FAIL
            if dict[k] == -1: dict[k] = FAIL

    for x in dict[1:]:
        print(x if x != -1 else 2)
