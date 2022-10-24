def func(n):
    if n == 3: # 0, 1, 8
        return 3 * 4
    if n == 2:
        return 4
    return func(n - 2) * 5
        

n = int(input())
print(func(n))