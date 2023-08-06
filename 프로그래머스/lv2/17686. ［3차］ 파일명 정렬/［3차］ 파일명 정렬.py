from functools import cmp_to_key

def getHeadAndNumber(s):
    
    headIdx = -1
    numbers = ''
    
    nFlag = False
    for idx in range(len(s)):
        # 문자인 경우, 이전에 숫자가 있었으면 tail 부분임
        if not s[idx].isdigit() and nFlag:
            break
        # 숫자인 경우, 이전이 숫자가 아니면 head
        if(s[idx].isdigit()) and not nFlag:
            headIdx = idx
            nFlag = True
        # 숫자인 경우, 이전이 숫자이면 연결
        if s[idx].isdigit():
            numbers += s[idx]
    head = s[0:headIdx]
    return head, int(numbers)

def solution(files):
    answer = []
    
    dict = {}
    for file in files:
        head, numbers = getHeadAndNumber(file)
        dict[file] = [head, numbers]
        
    # print(dict)
    
    def _cmp(x,y):
        [h_x, n_x] = dict[x]
        [h_y, n_y] = dict[y]
        
        if h_x.lower() > h_y.lower():
            return 1
        
        if h_x.lower() < h_y.lower():
            return -1
        
        
        if n_x > n_y:
            return 1
        if n_x < n_y:
            return -1
        return 0
    
    
    files.sort(key=cmp_to_key(_cmp))
    print(files)
    
    return files