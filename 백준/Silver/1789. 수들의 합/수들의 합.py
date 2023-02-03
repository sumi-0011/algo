import sys, math
from collections import deque

# sys.stdin = open('index.txt')
input = sys.stdin.readline

def  solution(s):
    cnt = 0
    res = 0
    if s == 1:
        return 1
    for i in range(1,s+1):
        res += i
        cnt +=1
        if res == s:
            return cnt
        if res >= s:
            return (cnt -1)

if __name__ == "__main__":
    s = int(input().strip())

    # tree = dict()
    # for i in range(1, n + 1):
    #     tree[i] = []
    #
    # for _ in range(n-1):
    #     n1, n2 = map(int, input().split())
    #     tree[n1].append(n2)
    #     tree[n2].append(n1)
    res = solution(s)
    print(res)