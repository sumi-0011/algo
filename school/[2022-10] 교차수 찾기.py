input()
arr1 = set(map(int, input().strip().split(' ')))
input()
arr2 = set(map(int, input().strip().split(' ')))
input()
arr3 = set(map(int, input().strip().split(' ')))

set = arr1 & arr2
set = set & arr3

print(len(set))
