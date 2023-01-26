import sys

input = sys.stdin.readline
def convert_binary(n):
    res = ''
    for _ in range(3):
        res = str(n % 2) + res
        n = n // 2
    return res

if __name__ == "__main__":
    n = input().strip()
    n = '0o' +n
    res = bin(int(n,8))
    print(res[2:])