# 입력
n = int(input())
arr = []
maxTime = 0
for _ in range(n):
    input()
    inArr = list(map(int, input().strip().split(' ')))
    arr.append(inArr)
    maxTime = inArr[-1] if inArr[-1] > maxTime else maxTime

result = [False for i in range(maxTime -1 )]

for person in arr:
    for i in range(0,len(person)//2):
        start = person[i * 2] - 1
        end = person[i * 2 + 1] -1
        for time in range(start,end):
            result[time] = True
        
start = -1
end = -1
res = 0
for idx in range(len(result)):
    if not result[idx]: #False
        if start != -1: #이전에 있었다면
            end = idx
        else: #처음 시작
            start = idx
            end = idx
    else:
        if start != -1 and end != -1:
            if start == end:
                res += (start + 1) * 2 + 1
            else: 
                res += (start +1) + (end + 2)
            start = -1
            end = -1
    
    
print(res)
        
        
