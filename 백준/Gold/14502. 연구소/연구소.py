import sys
from collections import deque

input = sys.stdin.readline

d = [(0,1),(0,-1),(1,0), (-1,0)]

def checkBirusNum(arr):
    N,M = len(arr), len(arr[0])
    visited = set()

    def dfs(start_node):
        stack = deque()
        stack.append(start_node)
        while stack:
            node = stack.pop()
            visited.add(node)

            for dx,dy in d:
                next = (node[0] + dx, node[1] + dy)
                if 0 <=next[0] < N and 0<= next[1] < M \
                        and next not in visited and arr[next[0]][next[1]] == 0:
                    stack.append(next)

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                dfs((i,j))

    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and (i,j) not in visited:
                res +=1

    return res

def checkEmptyPositions(arr):
    empty_list = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                empty_list.append((i,j))

    return empty_list

if __name__ == '__main__':
    n,m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    empty_list = checkEmptyPositions(arr)

    min_res = 0

    for i in range(0,len(empty_list)):
        for j in range(0, i):
            for k in range(0, j):
                node_i0, node_i1 = empty_list[i]
                node_j0, node_j1 = empty_list[j]
                node_k0, node_k1 = empty_list[k]
                arr[node_i0][node_i1] = 1
                arr[node_j0][node_j1] = 1
                arr[node_k0][node_k1] = 1
                res = checkBirusNum(arr)
                min_res = max(res, min_res)

                arr[node_i0][node_i1] = 0
                arr[node_j0][node_j1] = 0
                arr[node_k0][node_k1] = 0


    print(min_res)
