import sys


def count_cases(n):
    cnt3 = 4  # 모서리
    cnt2 = (n - 2) * 4 + (n - 1) * 4
    cnt1_top = (n - 2) ** 2
    cnt1_bottom = (n - 2) * (n - 1) * 4
    cnt1 = cnt1_top + cnt1_bottom
    return cnt1, cnt2, cnt3

def get_case2(n_dice):
    combination_2_not = [5, 4, 3, 2, 1, 0]  # set([(0, 5), (1, 3), (2, 4)])
    dice = n_dice.copy()
    sort_dice = sorted(dice)

    min_1, idx_1 = sort_dice[0], dice.index(sort_dice[0])

    dice[idx_1] = 50 # 값 없애기

    min_2, idx_2 = sort_dice[1], dice.index(sort_dice[1])
    if combination_2_not[idx_1] == idx_2:
        min_2 = sort_dice[2]

    return min_2 + min_1

def get_case3(dice):
    combination_3 = [(0, 1, 2), (0, 1, 3), (0, 3, 4), (0, 4, 2), (5, 1, 2), (5, 1, 3), (5, 3, 4), (5, 4, 2)]

    res = 50 * 6
    for x, y, z in combination_3:
        temp = dice[x] + dice[y] + dice[z]

        res = temp if res > temp else res
    return res

def get_cases(dice):
    sort_dice = sorted(dice)

    case_1 = sort_dice[0]
    case_2 = get_case2(dice)
    case_3 = get_case3(dice)

    return case_1, case_2, case_3


if __name__ == "__main__":
    # sys.stdin = open("index.txt", "r")

    N = int(sys.stdin.readline().rstrip())
    dice = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    if N == 1:
        res = sum(dice) - max(dice)
        print(res)
    else:
        case_1, case_2, case_3 = get_cases(dice)
        # print("case",case_1, case_2, case_3)
        cnt1, cnt2, cnt3 = count_cases(N)
        # print( "cnt", cnt1, cnt2, cnt3 )
        res = cnt1 *case_1 + cnt2 *case_2+ cnt3 *case_3
        print(res)
