def func(arr1, arr2):
    dict = {}
    for idx in range(len(arr1)):
        w1 = arr1[idx]
        w2 = arr2[idx]
        if w1 in dict.keys():
            # print(w1, '->/', w2)
            if dict[w1] != w2: return False
        else: 
            # print(w1, '->', w2)
            dict[w1] = w2
    return True
        
[str1, str2] = input().split(' ')

arr1 =  list(str1)
arr2 = list(str2)

print(func(arr1, arr2))
