import sys
from collections import deque

input = sys.stdin.readline

d = [(0,1),(0,-1),(1,0), (-1,0)]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        v,e = map(int, input().split())

        print(2-v+e)