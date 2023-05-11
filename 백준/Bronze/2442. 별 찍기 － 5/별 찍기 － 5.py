import sys

INF = int(1e9)

input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(i * 2 - 1):
        print('*', end='')
    for j in range(n - i):
        print('', end='')
    print()
