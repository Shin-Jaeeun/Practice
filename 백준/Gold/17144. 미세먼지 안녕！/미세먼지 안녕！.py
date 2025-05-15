import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# 방향: 상, 하, 좌, 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 공기청정기 위치(행번호만) 찾기
air = []
for i in range(R):
    if arr[i][0] == -1:
        air.append(i)

# 미세먼지 확산
def spread():
    # 매번 새로운 빈 temp 만들어줌 .. .. 이거 땜에 시간 그 난리인가
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                spread = arr[i][j] // 5
                count = 0
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    # 범위 내에 있고 & 공기 청정기 아니면
                    # 확산해주고, 확산 개수 1 더해주기
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        temp[ni][nj] += spread
                        count += 1
                temp[i][j] += arr[i][j] - spread * count
            elif arr[i][j] == -1:
                temp[i][j] = -1
    return temp

# 반대로 움직여야 영향 안받음
def clean_up():
    up = air[0]
    # 아래로
    for i in range(up - 1, 0, -1):
        arr[i][0] = arr[i - 1][0]
    # <-
    for j in range(C - 1):
        arr[0][j] = arr[0][j + 1]
    # 위로
    for i in range(up):
        arr[i][C - 1] = arr[i + 1][C - 1]
    # ->
    for j in range(C - 1, 1, -1):
        arr[up][j] = arr[up][j - 1]
    # 공기청정기 옆은 무조건 0
    arr[up][1] = 0

def clean_down():
    down = air[1]
    # 위로
    for i in range(down + 1, R - 1):
        arr[i][0] = arr[i + 1][0]
    # <-
    for j in range(C - 1):
        arr[R - 1][j] = arr[R - 1][j + 1]
    # 아래로
    for i in range(R - 1, down, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    # ->
    for j in range(C - 1, 1, -1):
        arr[down][j] = arr[down][j - 1]
    # 공기청정기 옆은 무조건 0
    arr[down][1] = 0

# T초 동안 확산 + 청소 반복
for _ in range(T):
    arr = spread()
    clean_up()
    clean_down()

# 미세먼지 합 구하기
total = 0
for i in range(R):
    for j in range(C):
        # 공기 청정기 계산에서 빼야되니까
        if arr[i][j] > 0:
            total += arr[i][j]

print(total)
