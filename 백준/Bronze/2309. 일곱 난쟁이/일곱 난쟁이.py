import sys
from itertools import combinations

input = sys.stdin.readline

MAX_SIZE = 1000000


def solution(arr):

    for combi in combinations(arr,7):
        if sum(combi) == 100:
            return sorted(combi)


if __name__ == "__main__":
    arr = []
    for _ in range(9):
        n = int(input())

        arr.append(n)
    res = solution(arr)
    for x in res:
        print(x)
    # print(res)
