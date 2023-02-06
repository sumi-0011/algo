import sys

input = sys.stdin.readline

def solution(a,b):
    prev = [0,1]
    for x in range(2,1001):
        for _ in range(x):
            prev.append(prev[-1] + x)

    print(prev[b] - prev[a -1])



if __name__ == "__main__":
    a,b = map(int, input().split())
    solution(a,b)