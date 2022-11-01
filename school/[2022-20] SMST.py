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

def twoKruskal(graph, noSelect):
    reserveSelect = (noSelect[0],noSelect[2],noSelect[1])
    otherEdges = list( set(graph['edges']) - set([noSelect,reserveSelect])  )
    mst = []

    # 초기화
    for node in graph['vertices']:
        initialization(node)

    # 간선을 오름차순으로 정렬
    edges = otherEdges
    edges.sort()

    # 사이클 확인 후 연결
    for edge in edges:
        weight, node_a, node_b = edge
        if find(node_a) != find(node_b):
            union(node_a, node_b)
            mst.append(edge)
    return mst
    
    
def getCnt(edgeList):
    res = 0
    for edge in edgeList:
        res += edge[0]
    return res

if __name__ == "__main__":
    N, M = map(int, input().split()) # split() 기본값은 공백 
    vertices =  input().split()

    edges = []

    for _ in range(M):
        a, b, value = map(str, input().split())
        edges.append((int(value),a, b))
        edges.append((int(value),b, a))
        
    graph = {
        'vertices' : vertices,
        'edges' : edges
    }
    

    minRes = kruskal(graph)

    twoMin = 50 * 100   # 최대값으로 초기화
    for restEdge in minRes:
        res = twoKruskal(graph, restEdge)
        cnt = getCnt(res)
        twoMin = twoMin if twoMin < cnt else cnt
        
    print(twoMin)    
    


 