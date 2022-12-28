import sys
 

def main():
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0:
        return True

    if a > b:
        print('Yes')
    else:
        print('No')
    return False
    # M = int(sys.stdin.readline())


if __name__ == "__main__":
    while True:
        if main():
            break
