import sys

if __name__ == "__main__":
    def inner_round(i, j):
        if i < 0 or j < 0 or j >= N or i >= N:
            return False
        return True


    def guess_water_copy(i, j):
        direction = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        cnt = 0
        for (x, y) in direction:
            ix, iy = i + x, j + y
            if inner_round(i + x, j + y):
                if arr[ix][iy] >= 1:
                    cnt += 1

        return cnt


    def position_move(position, moving):
        afterMove = position + moving
        if afterMove < 0 or afterMove >= N:
            return afterMove % N
        return afterMove


    def cloud_move(cloud, moving):
        x = position_move(cloud[0], moving[0])
        y = position_move(cloud[1], moving[1])
        return x, y


    def guess_next_cloud(clouds):
        nextCloud = []
        setClouds = set(clouds)
        for i in range(N):
            for j in range(N):
                if arr[i][j] >= 2 and not (i, j) in setClouds:
                    arr[i][j] -= 2  # 물이 2많큼 준다
                    nextCloud.append((i, j))
        return nextCloud


    def rain(clouds):
        for x, y in clouds:
            arr[x][y] += 1


    def water_copy(clouds):
        for x, y in clouds:
            # 물복사 버그
            arr[x][y] += guess_water_copy(x, y)


    def move(direction, size):
        global clouds
        #  ←, ↖, ↑, ↗, →, ↘, ↓, ↙
        moving = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        moveX, moveY = moving[direction - 1][0] * size, moving[direction - 1][1] * size

        newClouds = []
        for cloud in clouds:
            afterX, afterY = cloud_move(cloud, (moveX, moveY))
            newClouds.append((afterX, afterY))

        rain(newClouds)
        water_copy(newClouds)

        clouds = guess_next_cloud(newClouds)


    def result_sum():
        res = 0
        for i in range(N):
            for j in range(N):
                res += arr[i][j]
        return res


    N, M = map(int, sys.stdin.readline().rstrip().split(" "))
    arr = []
    for _ in range(N):
        inputArr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        arr.append(inputArr)

    clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

    # 이동
    for _ in range(M):
        d, s = map(int, sys.stdin.readline().rstrip().split(" "))
        move(d, s)

    print(result_sum())
