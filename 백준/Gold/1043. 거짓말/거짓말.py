import sys
input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a > b:
        change = parent[a]
        for i in range(1, len(parent)):
            if parent[i] == change:
                parent[i] = b
    else:
        change = parent[b]
        for i in range(1, len(parent)):
            if parent[i] == change:
                parent[i] = a


if __name__ == '__main__':
    n, m = map(int, input().split())

    # n = 사람의 수, m = 파티의 수
    t = list(map(int, input().split()))
    trust_people = t[1:]

    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i

    parts = []
    for _ in range(m):
        t = list(map(int, input().split()))
        if t[0] == 0:
            continue
        peoples = t[1:]
        parts.append(peoples)

        first_person = peoples[0]

        for idx in range(1, len(peoples)):
            person = peoples[idx]
            union(parent, first_person, person)

    know_people = set()

    for person in trust_people:
        p_parent = parent[person]
        for i in range(1, len(parent)):
            if parent[i] == p_parent:
                know_people.add(i)

    answer = 0
    for party in parts:
        flag = True
        for person in party:
            if person in know_people:
                flag = False
                break
        if flag:
            answer += 1

    print(answer)
