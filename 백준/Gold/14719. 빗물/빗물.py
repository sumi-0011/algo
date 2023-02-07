import sys

input = sys.stdin.readline


def calc(x, start_h, bottom_h):
    if start_h < x:
        return


def solution(h, w, hlist):
    sort_hlist = sorted(list(set(hlist)), reverse=True)

    closet_list = []
    result = {}
    for high_h in sort_hlist:
        for current_idx in range(len(hlist)):
            if hlist[current_idx] == high_h:
                closet_list.append(current_idx)

        closet_list.sort()
        # print(closet_list)
        if len(closet_list) >= 2:
            for idx in range(len(closet_list) - 1):
                for temp_idx in range(closet_list[idx] + 1, closet_list[idx + 1]):
                    # print(temp_idx, high_h)
                    if temp_idx not in result:
                        result[temp_idx] = high_h - hlist[temp_idx]

    sum=0
    for key in result:
        sum += result[key]
    return sum

if __name__ == "__main__":
    h, w = map(int, input().split())
    hlist = list(map(int, input().split()))
    res= solution(h, w, hlist)
    print(res)