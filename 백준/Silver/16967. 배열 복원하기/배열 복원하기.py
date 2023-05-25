import sys
from collections import deque
import copy

INF = float('inf')

d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
input = sys.stdin.readline

h, w, x, y = map(int, input().split())

arr_b = []
arr_a = []
for _ in range(h + x):
    t = list(map(int, input().split()))
    arr_b.append(t)

for _ in range(h):
    arr_a.append([0] * w)

for i in range(h + x):
    for j in range(w + y):
        if (0 <= i < h and 0 <= j < y) or (0 <= i < x and 0 <= j < w):
            arr_a[i][j] = arr_b[i][j]

for i in range(h + x):
    for j in range(w + y):
        if (h <= i < h + x and y <= j < w) or (x <= i < h and w <= j < w + y):
            arr_a[i - x][j - y] = arr_b[i][j]

for i in range(h + x):
    for j in range(w + y):
        if (x <= i < h and y <= j < w):
            arr_a[i][j] = arr_b[i][j] - arr_a[i - x][j - y]
for x in arr_a:
    print(" ".join(map(str, x)))
