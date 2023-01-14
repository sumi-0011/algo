import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def is_range(x, y, n, m):
    if 0 <= x <= n - 1 and 0 <= y <= m - 1:
        return True
    else:
        return False


def main(n, m, arr):
    visit = set()

    def bfs(start_node):
        queue = deque()
        queue.append(start_node)
        cnt = 0
        while queue:
            node = queue.popleft()
            if node not in visit and is_range(node[0], node[1], n, m) and arr[node[0]][node[1]] == 1:
                visit.add(node)
                cnt += 1
                for i in range(4):
                    queue.append((node[0] + dx[i], node[1] + dy[i]))
        return cnt

    res = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not (i, j) in visit:
                cnt = bfs((i, j))
                res.append(cnt)

    res.sort()
    print(len(res))
    for x in res:
        print(x)


if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, list(input().strip()))))

    main(n, n, arr)
