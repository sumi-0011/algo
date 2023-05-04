import heapq
import sys


input = sys.stdin.readline

n = int(input())

first = list(map(int, input().split()))

# max_arr = [first]
# min_arr = [first]

max_prev = first
min_prev = first

for idx in range(1, n):
    t = list(map(int, input().split()))

    max_1 = max(max_prev[0:2]) + t[0]
    max_2 = max(max_prev) + t[1]
    max_3 = max(max_prev[1:]) + t[2]

    max_prev = [max_1, max_2, max_3]
    # max_arr.append([max_1, max_2, max_3])

    min_1 = min(min_prev[0:2]) + t[0]
    min_2 = min(min_prev) + t[1]
    min_3 = min(min_prev[1:]) + t[2]
    min_prev = [min_1, min_2, min_3]
    # min_arr.append([min_1, min_2, min_3])

mmax = max(max_prev)
mmin = min(min_prev)

print(mmax, mmin)
