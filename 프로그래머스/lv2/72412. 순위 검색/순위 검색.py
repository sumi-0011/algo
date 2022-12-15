import bisect, itertools, collections

def solution(info, query):
    answers = []
    arr = {}

    for person in info:
        infoList = person.split(" ")
        list = []

        def getInfo(li, idx):
            if idx == 4:
                list.append(" and ".join(li))
                return
            li1 = li + [infoList[idx]]
            li2 = li + ['-']
            getInfo(li1, idx + 1)
            getInfo(li2, idx + 1)

        getInfo([], 0)

        for custominfo in list:
            if not custominfo in arr:
                arr[custominfo] = []

            arr[custominfo].append(int(infoList[4]))

    for k in arr.keys():
        arr[k].sort()
        
    for q in query:
        l,_,p,_,c,_,f, point = q.split()
        key = ' and '.join([l,p,c,f])
        if key in arr:
            i = bisect.bisect_left(arr[key], int(point))
            answers.append(len(arr[key]) - i)
        else:
            answers.append(0)
            
    return answers