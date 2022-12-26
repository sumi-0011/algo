import sys


def func(s):
    ae = set(['a', 'e', 'i', 'o', 'u'])
    cnt = 0
    for x in list(s):
        if x.lower() in ae:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    while True:
        s = sys.stdin.readline().strip()
        if s == '#':
            break

        res = func(s)
