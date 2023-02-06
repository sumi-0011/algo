def solution(board):
    answer = 0
    visited = set()
    n = len(board)
    
    def check_wlhl(i,j):
         for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                visited.add((x,y))
                # if 0<= x < n and 0<= y < n:
                #     if board[x][y]
    def check_safe(i,j):
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if 0<= x < n and 0<= y < n:
                    if board[x][y] == 1:
                        return False
        return True
    
    for i in range(n):
        for j in range(n):
            if (i, j) in visited:
                continue
            if board[i][j] == 1:
                check_wlhl(i,j)
                continue
            # 지뢰 x 안전 지대인지 확인
            if check_safe(i,j):
                answer +=1
    return answer