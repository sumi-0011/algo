import sys


input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}
for i in range(0, 10):
    dict[i] = 0

for x in range(1, n + 1):
    s = str(x)
    li = list(map(int, list(s)))
    for i in li:
        dict[i] += 1

print(dict[m])
