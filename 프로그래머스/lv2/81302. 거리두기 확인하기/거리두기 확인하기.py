def mentaton(r1,c1,r2,c2):
    return abs(r1-r2) + abs(c1,c2)
def check_range(r,c,arr):
    N = len(arr)
    if 0<=r<N and 0<=c<N:
        return True
    return False

def check_diagonal(arr,r,c):
    person = [(-1,-1),(-1,1),(1,1),(1,-1)]
    
    for dx,dy in person:
        x,y = r + dx,c+dy
        
        if check_range(x,y,arr) and arr[x][y] == 'P':
            if arr[x][c] == 'X' and arr[r][y] == 'X':
                continue
            else:
                print(r,c)
                return False
    return True
    
def check_line(arr, r,c):
    person = [(-1,0),(0,1),(1,0),(0,-1)]
    
    for dx,dy in person:
        for i in range(1,3):

            x,y = r + dx * i,c+dy *i
            if check_range(x,y,arr) and arr[x][y] == 'P':
                if arr[r+dx][c+dy] != 'X':
                    print(r,c)
                    return False
    return True
    
def check(arr, r,c):
    if not check_line(arr, r,c):
        return False
    if not check_diagonal(arr, r,c):
        return False
    return True

def main(place):
    print('----')
    arr = []
    for row in place:
        arr.append(list(row))
    
    for r in range(5):
        for c in range(5):
            if arr[r][c] == 'P':
                if not check(arr,r,c):
                    return False
    return True
def solution(places):
    answer = []
    
    for place in places:
        res = main(place)
        answer.append(1) if res else answer.append(0)
    
    
    return answer