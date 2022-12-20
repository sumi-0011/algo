import sys

def jun(m, arr):
    cnt = 0
    money = m
    for x in arr:
        cnt += money // x
        money = money % x

    return cnt * arr[-1] + money


def sung(m, arr):
    down_cnt = 0
    up_cnt = 0
    money = m
    purchase_cnt = 0
    result = 0
    for i in range(1, len(arr)):
        if up_cnt >= 3:
            price = arr[i - 1]
            result += price * purchase_cnt
            purchase_cnt = 0
            money += price * purchase_cnt

        if down_cnt >= 3:
            price = arr[i - 1]
            purchase_cnt += money // price
            money = money % price

        if arr[i - 1] < arr[i]:  # 증가
            up_cnt += 1
            down_cnt = 0
        elif arr[i - 1] > arr[i]:
            down_cnt += 1
            up_cnt = 0
        else:
            up_cnt = 0
            down_cnt = 0

    result += purchase_cnt * arr[-1]
    return result + money


if __name__ == "__main__":

    M = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    jun_m = jun(M, arr)
    sung_m = sung(M, arr)
    if jun_m == sung_m:
        print("SAMESAME")
    elif jun_m > sung_m:
        print("BNP")
    else:
        print("TIMING")
