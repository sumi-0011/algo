import math
import sys



def main(N, M):
    return (math.factorial(N) // (math.factorial(N - M) * math.factorial(M)))


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    print(main(N, M)) 
