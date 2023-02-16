import sys
T = int(input())

for test_case in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    print(N-1)