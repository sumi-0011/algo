import sys

INF = int(1e9)


input = sys.stdin.readline

s = input().strip()
dic = {}
for x in range(ord('a'), ord('z') + 1):
    dic[chr(x)] = 0
for x in s:
    dic[x] += 1
arr = list(dic.keys())
arr.sort()

for key in arr:
    print(dic[key], end=' ')
