import sys
from queue import PriorityQueue


def sol(N, M, K):
    que = PriorityQueue()
    arr = []
    for _ in range(K):
        v, c = map(int, sys.stdin.readline().split())
        arr.append((c, v))

    arr.sort(key=lambda x: x[0])
    res_m = 0
    for c, v in arr:
        que.put((v, c))
        res_m += v
        # print((v, c))
        if que.qsize() > N:
            # 금방 추가한 맥주가 N이상 -> 뭔가를 빼야함
            delete = que.get()
            # print('delete', delete)
            res_m -= delete[0]

        if res_m >= M and que.qsize() == N:
            return c
    return -1


if __name__ == "__main__":

    N, M, K = map(int, sys.stdin.readline().split())
    res = sol(N, M, K)
    print(res)
