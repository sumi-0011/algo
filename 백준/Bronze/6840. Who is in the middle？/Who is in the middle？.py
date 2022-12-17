import sys

if __name__ == "__main__":
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())

    arr = [a, b, c]
    arr.sort()

    print(arr[1])
