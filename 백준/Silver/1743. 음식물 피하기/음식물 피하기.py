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
            if node not in visit and is_range(node[0], node[1], n, m) and node in arr:
                visit.add(node)
                cnt += 1
                for i in range(4):
                    queue.append((node[0] + dx[i], node[1] + dy[i]))
        return cnt

    res = []
    for r, c in arr:
        t = bfs((r, c))
        res.append(t)

    return max(res)


if __name__ == "__main__":
    n, m, k = map(int, input().split())

    arr = []
    for _ in range(k):
        r, c = map(int, input().split())
        arr.append((r - 1, c - 1))

    res = main(n, m, set(arr))
    print(res)
