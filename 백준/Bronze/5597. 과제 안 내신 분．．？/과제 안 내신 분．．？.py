import sys
from itertools import combinations

input = sys.stdin.readline



def solution(arr):
    t = set(arr)
    res = []
    for x in range(1,31):
        if x not in t:
            res.append(x)
    res.sort()

    print(res[0])
    print(res[1])

if __name__ == "__main__":
    arr = []
    for _ in range(28):
        arr.append(int(input().strip()))
    res = solution(arr)
