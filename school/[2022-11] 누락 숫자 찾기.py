input()
arr = list(map(int, input().strip().split(' ')))
k = int(input())

cnt = 1
res = 0
for n in range(arr[0], 10001):
    if len(arr) > 0 and n == arr[0]:
        arr = arr[1:]
    else:
        if cnt == k:
            print(n)
            res = n
            break
        cnt+=1
