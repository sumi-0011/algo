[str1, str2] = input().split(' ')

sort1 = sorted(list(str1))
sort2 = sorted(list(str2))

flag = True
if len(str1) != len(str2): 
    flag = False
else:
    for idx in range(0,len(sort1)):
        if(sort1[idx] == sort2[idx]): continue
        else: flag = False

print(flag)