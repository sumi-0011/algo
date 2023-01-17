import sys

input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        s = input().strip()
        if s == 'END':
            break
        t = list(s)
        t.reverse()

        print("".join(t))