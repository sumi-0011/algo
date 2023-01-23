import sys

input = sys.stdin.readline

if __name__ == "__main__":
    # t = int(input())
    people = 0
    max_people = 0
    for _ in range(10):
        n,m= map(int, input().split())
        people = people + m - n
        max_people = max(max_people, people)
    print(max_people)