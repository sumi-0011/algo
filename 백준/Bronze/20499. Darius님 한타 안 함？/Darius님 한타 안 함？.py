if __name__ == "__main__":
    k, d, a = map(int, input().split('/'))
    if k + a < d or d == 0:
        print('hasu')
    else:
        print('gosu')