import sys

input = sys.stdin.readline

def main(n):
    temp = n
    res = ''
    while temp // 2 != 0:
        t = temp % 2
        res = str(t) + res
        temp = temp // 2
    res = str(temp) + res
    res = list(res)
    res.reverse()
    arr = []
    for idx in range(len(res)):
        if res[idx] =='1':
            print(idx, end=' ')
            # arr.append(idx)
    print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        main(n)
