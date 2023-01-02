import sys


def main(name, age, weight):
    if age > 17 or weight >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")
    return 0


if __name__ == "__main__":
    while True:
        name, a, w = map(str, sys.stdin.readline().strip().split())

        if name == "#":
            break
        main(name, int(a), int(w))
