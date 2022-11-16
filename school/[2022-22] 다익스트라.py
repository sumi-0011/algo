def init():
    global graph, infinity, costs, parents, processed
    graph = {} # 간선 정보 입력

    nodeL , edgeL = map(int, input().split(" "))
    start, end = input().split(" ")
    nodes = input().split(" ")

    for node in graph:
        print(node)
        graph[node] = {}
    
    for _ in range(edgeL):
        a,b,cost = input().split(" ")
        cost = int(cost)
        if not a in graph:
          graph[a] = {}
        if not b in graph:
            graph[b] = {}
        graph[a][b] = cost
        graph[b][a] = cost
    
    
    infinity = float("inf")

    costs = {} # 해당 노드 최단경로 입력
    for node in nodes:
        costs[node] = infinity
        
   
    parents = {} # 추적 경로를 위해 부모 설정
    for node in nodes:
        parents[node] = None
 
    processed = []

    return (start, end)

# 최단 경로를 가진 노드를 구한다.
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

# 다익스트라 알고리즘
def dijkstra(graph, start, final):
    node = start
    costs[start] = 0
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost: # 현재 가지고있는 cost보다 new_cost가 더 최단거리라면
                costs[n] = new_cost # 갱신
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    # 경로 추적 로직
    trace = []
    current = final
    while current != start:
        trace.append(current)
        current = parents[current]
    trace.append(start)
    trace.reverse()
    # print("=== Dijkstra ===")
    # print(start, "에서 ", final, "까지의 정보")
    # print("최단 거리 : ", costs[final])
    # print("진행 과정 : ", processed)
    # print("경로 : ", trace)

    print("".join(trace))
    print( costs[final])

if __name__ == "__main__":

    graph = {}
    infinity = float("inf")
    costs = {}
    parents = {}
    processed = []


    start, end = init()
    dijkstra(graph, start, end )