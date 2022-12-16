import sys

def getSystemString(n, system):
    res = ""
    while True:
        if n < system:
            res = str(n) + res
            break
        t = n % system
        n = n // system
        res = str(t) + res
    return res


def isPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - i - 1]:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    result = []
    for i in range(2, 11):
        s = getSystemString(N, i)
        if isPalindrome(s):
            result.append((i, s))

    if len(result) == 0:
        print("NIE")
    else:
        for i, s in result:
            print(i, s)
