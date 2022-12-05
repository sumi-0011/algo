import sys


if __name__ == "__main__":
    #sys.stdin = open("index.txt", "r")

    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    v= int(sys.stdin.readline().rstrip())

    cnt = 0
    for x in arr:
        if x == v:
            cnt +=1
    print(cnt)