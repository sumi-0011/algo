import sys

input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
stack = []
visited = set()


def dfs():
    if len(stack) == m:
        t = ' '.join(list(map(str, stack)))
        if t not in visited:
            print(t)
            visited.add(t)
        return

    for x in arr:
        if len(stack) and stack[-1] > x:
            continue
        stack.append(x)
        dfs()
        stack.pop()


dfs()
#
# visited = list(visited)
# visited.sort()
#
# for x in visited:
#     print(x)
