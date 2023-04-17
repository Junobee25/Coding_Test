# 문제
# 스타트팀 능력치의 합과
# 링크팀 능력치의 합의 차이의 최솟값을 구하는 문제
# 능력치 계산 => arr[i][j] + arr[j][i]
# 스타트팀 모든 경우의수
# 링크팀 모든 경우의 수
# 스타트팀에서 뽑힌 인원은 링크팀에서 없어야 함

# 접근
# 완전탐색 combinations
# 시간복잡도 20
from itertools import combinations
from copy import deepcopy
N = int(input())
# combi 구하기 위해 사람들의 번호 나열
combi = [i for i in range(1,N+1)]
matrix = []

for _ in range(N):
    matrix.append(list(map(int,input().split())))

min_val = int(1e9)

for x in combinations(combi,N//2):
    combi2 = deepcopy(combi)
    for i in x:
        combi2.remove(i)

    start = 0
    for x1 in combinations(x,2):

        start += matrix[x1[0]-1][x1[1]-1] + matrix[x1[1]-1][x1[0]-1]

    for y in combinations(combi2,N//2):
        # x에서 뽑힌 친구들은 y에 있으면 안됨
        link = 0
        for y1 in combinations(combi2,2):
            link += matrix[y1[0]-1][y1[1]-1] + matrix[y1[1]-1][y1[0]-1]


        if abs(start - link) <= min_val:
            min_val = abs(start - link)
print(min_val)