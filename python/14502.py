import sys


def bfs(start_node):
    global visit, board
    queue = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)

        if node not in visit:
            visit.append(node)
            print(node)
            queue.extend(board[node])

    return visit


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []
visit = [[False] * M  for _ in range(N)]
