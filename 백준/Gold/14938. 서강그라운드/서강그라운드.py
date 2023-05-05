import sys

INF = int(1e9)

input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = {}
for x in range(1, n + 1):
    graph[x] = []

for _ in range(r):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))


def dijkstra(start):
    visited = set()
    distance = [INF for _ in range(n + 1)]

    def get_short_node():
        idx = 1
        min_val = INF
        for i in range(1, n + 1):
            if i not in visited and distance[i] < min_val:
                min_val = distance[i]
                idx = i
        return idx

    visited.add(start)
    distance[start] = 0

    for next, cost in graph[start]:
        distance[next] = cost

    for i in range(1, n + 1):
        current = get_short_node()
        visited.add(current)

        for next, cost in graph[current]:
            distance[next] = min(distance[next], distance[current] + cost)

    return distance


def get_item_count(start):
    distance = dijkstra(start)[1:]
    res = 0
    for i in range(n):
        if distance[i] <= m:
            res += items[i]

    return res


max_res = 0
for i in range(1, n + 1):
    res = get_item_count(i)
    max_res = max(max_res, res)

print(max_res)
