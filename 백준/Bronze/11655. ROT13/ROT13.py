import sys

input = sys.stdin.readline


def change(c):
    if ord('A') <= ord(c) <= ord('Z'):
        res = ord(c) + 13
        return res if ord(c) + 13 <= ord('Z') else res + (ord('A') - ord('Z') - 1)
    if ord('a') <= ord(c) <= ord('z'):
        res = ord(c) + 13
        return res if ord(c) + 13 <= ord('z') else res + (ord('a') - ord('z') - 1)

    return ord(c)


def main(s):
    res = ''
    for x in s:
        if ord('A') <= ord(x) <= ord('z'):
            res += chr(change(x)).strip()
        else:
            res += x
    return res


if __name__ == "__main__":
    s = input()

    print(main(s))
