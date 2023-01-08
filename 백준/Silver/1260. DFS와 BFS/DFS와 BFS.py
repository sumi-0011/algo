import sys
from collections import deque


def main(graph, start):
    dfs(graph, start)
    print()
    bfs(graph, start)


def bfs(graph, start):
    visited = set()
    queue = deque()

    queue.append(start)

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
            print(node, end=' ')
    return visited


def dfs(graph, start):
    visited = set()

    stack = deque()

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            stack.extend(sorted(graph[node], reverse=True))
            print(node, end=' ')

    return visited


if __name__ == "__main__":
    n, m, v = map(int, sys.stdin.readline().split())
    graph = {}

    for x in range(1, n + 1):
        graph[x] = []

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for x in graph:
        graph[x] = sorted(graph[x])
    main(graph, v)
    # print(main(graph, v))
