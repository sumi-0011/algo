import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n,q = map(int, input().split())

    arr = []
    for i in range(n):
        time = int(input())
        arr += [i +1] * time

    for x in range(q):
        que = int(input())
        print(arr[que])
