import sys, math
from collections import deque

input = sys.stdin.readline

def  solution(n, tree):
    q = deque([1])
    parent = [0] * (n + 1)
    while(q) :
        current = q.popleft()
        for i in tree[current]:
            if parent[i] == 0 and i!=1:
                parent[i] = current
                q.append(i)
    for i in range(2, n+1):
        print(parent[i])
if __name__ == "__main__":
    n = int(input().strip())

    tree = dict()
    for i in range(1, n + 1):
        tree[i] = []

    for _ in range(n-1):
        n1, n2 = map(int, input().split())
        tree[n1].append(n2)
        tree[n2].append(n1)
    solution(n, tree)