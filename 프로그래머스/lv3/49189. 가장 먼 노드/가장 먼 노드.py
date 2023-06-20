from collections import deque
INF = 10 ** 6

def solution(n, edge):
    dict = {}
    
    for i in range(1, n+1):
        dict[i] = []
    for a,b in edge:
        dict[a].append(b)
        dict[b].append(a)
    
    def find_c(start):
        arr = [INF for _ in range(n+1)]
        arr[start] = 1
        
        stack = deque()
        visited = set()
        for edge in dict[start]:
            arr[edge] = 1
            stack.append(edge)
            visited.add(edge)
        
        while stack:
            current = stack.popleft()
            
            for edge in dict[current]:
                if edge in visited:
                    continue
                arr[edge] = min(arr[current] + 1, arr[edge])
                visited.add(edge)
                stack.append(edge)
        print(arr)
        
        max_n = max(arr[1:])
        return arr.count(max_n)
    res = find_c(1)
        
    
    
    return res