from copy import deepcopy
N,M,y,x,K = map(int,input().split())

# 초기 주사위 상태
# 위 뒤 동 서 앞 아래
dice = [0,0,0,0,0,0]

def rolling(direct):
    global dice
    my_dice = deepcopy(dice)
    # 동쪽으로 이동 후 주사위 상태
    if direct == 1:
        my_dice[2] = dice[0]
        my_dice[5] = dice[2]
        my_dice[0] = dice[3]
        my_dice[3] = dice[5]
        dice = my_dice
    # 서쪽으로 이동 후 주사위 상태
    elif direct == 2:
        my_dice[3] = dice[0]
        my_dice[0] = dice[2]
        my_dice[5] = dice[3]
        my_dice[2] = dice[5]
        dice = my_dice
    # 북쪽으로 이동 후 주사위 상태
    elif direct == 3:
        my_dice[1] = dice[0]
        my_dice[5] = dice[1]
        my_dice[0] = dice[4]
        my_dice[4] = dice[5]
        dice = my_dice
    # 남쪽으로 이동 후 주사위 상태
    elif direct == 4:
        my_dice[4] = dice[0]
        my_dice[0] = dice[1]
        my_dice[5] = dice[4]
        my_dice[1] = dice[5]
        dice = my_dice


# 지도
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

# 방향 벡터
# 동 서 북 남
dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]

# 명령

cmd = list(map(int,input().split()))

# 지도 상에서 주사위 굴리기
# 주사위가 처음에 있는 좌표는 board[y][x]
for t in cmd:
    if (0<=y+dy[t]<N) and (0<=x+dx[t]<M):
        y += dy[t]
        x += dx[t]
        rolling(t)
    else:
        continue
    if board[y][x] == 0:
        board[y][x] = dice[-1]
    elif board[y][x] != 0:
        dice[-1] = board[y][x]
        board[y][x] = 0

    print(dice[0]) 
