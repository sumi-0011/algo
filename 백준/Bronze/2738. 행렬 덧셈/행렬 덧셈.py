import sys


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split(" "))

    arr1 = []
    for _ in range(N):
        temp = sys.stdin.readline()
        arr1.append(temp)

    for i in range(N):
        temp1 = list(map(int, arr1[i].split(" ")))
        temp2 = list(map(int, sys.stdin.readline().split(" ")))

        for j in range(M):
            res = temp1[j] + temp2[j]
            print(res, end=" ")
        print()
