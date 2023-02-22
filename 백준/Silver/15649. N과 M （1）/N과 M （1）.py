import sys
from itertools import permutations

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = [str(x) for x in range(1, n+1)]

    res = []
    for combi in permutations(arr, m):
        t = list(combi)
        # t.sort()
        res.append(" ".join(t))

    res.sort()

    for x in res:
        print(x)
