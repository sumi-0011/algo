import sys

input = sys.stdin.readline



def get_dicisor(n):
    data = set()

    for i in range(1, int(n ** (1/2)) +1):
        if n % i == 0:
            data.add(i)
            data.add(n // i)
    return sorted(data)

def main(n,k):

    arr = get_dicisor(n)
    if len(arr) >= k:
        return arr[k-1]
    else:
        return 0


if __name__ == "__main__":
    n,k = map(int, input().split())
    print(main(n,k))
