import sys
from collections import deque

INF = int(1e9)


input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

while True:
    M, N = map(int, input().split())
    if N == 0:
        break

    arr = []
    for _ in range(N):
        arr.append(list(map(int, list(input().split()))))

    visited = set()


    def dfs(start):
        stack = deque()
        stack.append(start)
        visited.add(start)
        cnt = 0
        while stack:
            current = stack.pop()
            cnt += 1
            for dx, dy in d:
                nex = (current[0] + dx, current[1] + dy)
                if 0 <= nex[0] < N and 0 <= nex[1] < M and arr[nex[0]][nex[1]] == 1 and nex not in visited:
                    stack.append(nex)
                    visited.add(nex)
        return cnt


    res = []
    res_count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and (i, j) not in visited:
                res_count += 1
                res.append(dfs((i, j)))

    print(res_count)
