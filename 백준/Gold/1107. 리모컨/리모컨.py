import sys
from itertools import product


def action_cnt(n, combin_num):
    return abs(combin_num - n)


def main():
    N_str = sys.stdin.readline().strip()
    M = int(sys.stdin.readline())
    cnt = 5000000
    arr = list(map(int, sys.stdin.readline().split()))
    all_btns = set([i for i in range(0, 10)])
    correct = list(map(str, all_btns - set(arr)))

    if M == 0:
        return min(len(N_str), abs(int(N_str) - 100))
    if M == 10:
        return abs(int(N_str) - 100)

    for i in range(-1, 2):
        if len(N_str) + i <= 0: continue
        for cwr in product(correct, repeat=len(N_str) + i):
            combin_num = int("".join(cwr))
            cnt = min(cnt, action_cnt(int(N_str), combin_num) + len(str(combin_num)))
            # print((combin_num, action_cnt(int(N_str), combin_num) + len(str(combin_num))))
    if abs(int(N_str) - 100) < cnt:
        return abs(int(N_str) - 100)

    return cnt


if __name__ == "__main__":
    answer = main()

    print(answer)
    # print("answer", answer)
