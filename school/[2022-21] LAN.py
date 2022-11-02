# 부모 노드 값 저장
parent = dict()
# 각각의 노드의 높이 번호
rank = dict()

def initialization(node):
    parent[node] = node
    rank[node] = 0

def find(node):
    # path compression
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_a, node_b):
    # union-by-rank
    root_a = find(node_a)
    root_b = find(node_b)

    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1

def kruskal(graph):
    mst = []

    # 초기화
    for node in graph['vertices']:
        initialization(node)

    # 간선을 오름차순으로 정렬
    edges = graph['edges']
    edges.sort()

    # 사이클 확인 후 연결
    for edge in edges:
        weight, node_a, node_b = edge
        if find(node_a) != find(node_b):
            union(node_a, node_b)
            mst.append(edge)

    return mst

if __name__ == "__main__":
    town, connect_limit= map(int, input().strip().split(' '))
    satelite_build_cost = list(map(int, input().strip().split(' ')))
    
    edges = []

    for idx in range(len(satelite_build_cost)):
        cost = satelite_build_cost[idx]
        edges.append((cost, 0, idx+1))

    for _ in range(connect_limit):
        m1, m2 ,connect_cost=  map(int, input().strip().split(' '))
        edges.append((connect_cost, m1, m2))
        edges.append((connect_cost, m2, m1))

    graph = {
        'vertices' : [i for i in range(town +1) ],
        'edges' : edges
    }
    
    res =  kruskal(graph)
    result = 0
    for edge in res:
        result += edge[0]
    print(result)
