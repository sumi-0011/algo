import heapq
import sys

INF = int(1e9)

input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def func(graph, start, end):
    visited = set()
    min_res = 10 ** 6

    def _func(current, cnt):
        if current == end:
            return cnt
        min_t = 10 ** 6
        for nex in graph[current]:
            if nex not in visited:
                min_t = min(min_t, _func(nex, graph[current][nex] + cnt))
        return min_t

    res = _func(start, 0)
    print(res)
    return res


n, m, x = map(int, input().split())

graph = [[] for i in range(n + 1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))


def get_short_path(start):
    distance = [INF] * (n + 1)

    def dijkstra(start):
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0
        # q가 비어있지 않다면
        while q:
            # 가장 최단 거리인 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리됐다면 skip
            if distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드 확인
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거치면 이동 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    # 다익스트라 알고리즘 실행
    dijkstra(start)

    return distance


in_distances = get_short_path(x)

answer = 0
for start in range(1, n + 1):
    out = get_short_path(start)[x]

    answer = max(answer, out + in_distances[start])
print(answer)
