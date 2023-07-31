from collections import deque

def check_ok(arr):
    stack = deque()
    
    for x in arr:
        # if stack:
        if x in ['[', '(', '{']:
            stack.append(x)
        else:
            if not stack:
                return False
            current = stack.pop()
            if x == ']' and current != '[':
                return False
            if x == ')' and current != '(':
                return False
            if x == '}' and current != '{':
                return False
    if stack:
        print('stack not empty')
        return False
    return True
            

def move_rhkfgh(s):
    queue = deque(s)
    list = [s]
    for i in range(len(s)-1):
        t = queue.popleft()
        queue.append(t)
        st = str(''.join(queue))
        # print(st)
        list.append(st)
    return list
    # print(s[1:-1])
        
    

def solution(s):
    answer = 0
    
    for t in move_rhkfgh(s):
        res = check_ok(t)
        if res:
            answer +=1
    return answer