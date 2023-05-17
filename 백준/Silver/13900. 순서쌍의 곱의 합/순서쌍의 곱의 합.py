import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split(" ")))

prev_sum = []
total_sum = sum(arr)
for x in arr:
    if len(prev_sum) == 0:
        prev_sum.append(x)
        continue
    prev_sum.append(x + prev_sum[-1])

res = 0
for i in range(n):
    current = arr[i]
    multi_sum = total_sum - prev_sum[i]
    res += multi_sum * current

print(res)
