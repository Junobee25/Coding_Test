n,m = map(int,input().split())
y,x,d = map(int,input().split())

# d => 방향
# {0:북,1:동,2:남,3:서}

# 청소된 칸을 7로 바꾸기
cnt = 0
room = []


# 후진 메소드
def is_posible_back(y,x,t):
    # 현재 북쪽을 보고 있다
    if t == 0:
        # 남쪽이 행렬 내부에 있고
        if 0<=y+dy[2]<n and 0<=x+dx[2]<m:
            # 벽이 아니라면
            if room[y+dy[2]][x+dx[2]] != 1:
                return True
    # 현재 동쪽을 보고 있다
    elif t == 1:
        # 서쪽이 행렬 내부에 있고
        if 0<=y+dy[3]<n and 0<=x+dx[3]<m:
            # 벽이 아니라면
            if room[y+dy[3]][x+dx[3]] != 1:
                return True
    # 현재 남쪽을 보고 있다
    elif t == 2:
        # 남쪽이 행렬 내부에 있고
        if 0<=y+dy[0]<n and 0<=x+dx[0]<m:
            # 벽이 아니라면
            if room[y+dy[0]][x+dx[0]] != 1:
                return True
    # 현재 서쪽 을 보고 있다.
    else:
        # 동쪽이 행렬 내부에 있고
        if 0<=y+dy[1]<n and 0<=x+dx[1]<m:
            # 벽이 아니라면
            if room[y+dy[1]][x+dx[1]] != 1:
                return True
    # 그렇지 않으면 갈 수 없음        
    return False

# 회전 후 청소 (청소되지 않은 칸이 나올 때까지 반시계 방향으로 회전하기)
def rotation_go(y,x,t):
    global d
    # 현재 북쪽을 보고 있다 => 서(-1) 남(-2) 동(-3) 북(-4)
    if t == 0:
        ry = [0,1,0,-1]
        rx = [-1,0,1,0]
        for i in range(4):
            if 0<=y+ry[i]<n and 0<=x+rx[i]<m:
                # 청소안한 구역
                if room[y+ry[i]][x+rx[i]] == 0:
                    if i == 0:
                        d = 3
                    elif i == 1:
                        d = 2
                    elif i == 2:
                        d = 1
                    else:
                        d = 0
                    return True
    # 현재 동쪽을 보고 있다 => 북 서 남 동
    elif t == 1:
        ry = [-1,0,1,0]
        rx = [0,-1,0,1]
        for i in range(4):
            if 0<=y+ry[i]<n and 0<=x+rx[i]<m:
                # 청소안한 구역
                if room[y+ry[i]][x+rx[i]] == 0:
                    if i == 0:
                        d = 0
                    elif i == 1:
                        d = 3
                    elif i == 2:
                        d = 2
                    else:
                        d = 1
                    return True
    # 현재 남쪽을 보고 있다 => 동 북 서 남
    elif t == 2:
        ry = [0,-1,0,1]
        rx = [1,0,-1,0]
        # 남쪽이 행렬 내부에 있고
        for i in range(4):
            if 0<=y+ry[i]<n and 0<=x+rx[i]<m:
                # 청소안한 구역
                if room[y+ry[i]][x+rx[i]] == 0:
                    if i == 0:
                        d = 1
                    elif i == 1:
                        d = 0
                    elif i == 2:
                        d = 3
                    else:
                        d = 2
                    return True
    # 현재 서쪽 을 보고 있다. => 남 동 북 서
    else:
        ry = [1,0,-1,0]
        rx = [0,1,0,-1]
        # 동쪽이 행렬 내부에 있고
        for i in range(4):
            if 0<=y+ry[i]<n and 0<=x+rx[i]<m:
                # 청소안한 구역
                if room[y+ry[i]][x+rx[i]] == 0:
                    if i == 0:
                        d = 2
                    elif i == 1:
                        d = 1
                    elif i == 2:
                        d = 0
                    elif i == 3:
                        d = 3
                    return True
for _ in range(n):
    room.append(list(map(int,input().split())))

# 방향 벡터 북 동 남 서
# y,x 는 초기 좌표
dy = [-1,0,1,0]
dx = [0,1,0,-1]
while True:
    if room[y][x] == 0:
        room[y][x] = 7
        cnt += 1
    check = 0
    # 상하좌우에 청소되지 않은 구역이 있는지 판단
    for i in range(4):
        if 0<= y + dy[i] < n and 0<= x + dx[i] < m:
            y += dy[i]
            x += dx[i]
            if room[y][x] == 0:
                check += 1
        # 원래 자리 복귀
        y -= dy[i]
        x -= dx[i]
    # 청소되지 않은 빈 칸이 없을 때
    if check == 0:
        # 바라보는 방향 유지한 채로 한 칸 후진 할 수 있다면 한칸 후진
        if is_posible_back(y,x,d):
            if d == 0:
                y += dy[2]
                x += dx[2]

            elif d == 1:
                y += dy[3]
                x += dx[3]

            elif d == 2:
                y += dy[0]
                x += dx[0]

            elif d == 3:
                y += dy[1]
                x += dx[1]

        # 벽이라 한칸 후진하지 못하면 작동 멈춤
        else:
            break
    # 청소되지 않은 빈 칸이 있을 경우
    else:
        if rotation_go(y,x,d): # 빈칸 중에 어디로 가야할지 인덱스가 정해짐 방향인덱스가 정해짐 (d)
            y += dy[d]
            x += dx[d]

print(cnt)