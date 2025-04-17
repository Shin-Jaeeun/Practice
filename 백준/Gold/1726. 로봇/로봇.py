from collections import deque
import sys
input = sys.stdin.readline
di = [0,0,1,-1]
dj = [1,-1,0,0]
def bfs():
    queue = deque()
    queue.append((start_r,start_c,start_dir))
    visited[start_r][start_c][start_dir] = 1
    while queue:
        r,c,dir = queue.popleft()

        # 종료 조건
        if (r,c,dir) == (last_r,last_c,last_dir):
            print(visited[r][c][dir]-1)
            return

        # Go k
        for k in range(1,4):
            nr = r+di[dir-1] * k
            nc = c+dj[dir-1] * k

            # 범위 벗어나면 종료
            if not (0 <= nr < M and 0 <= nc < N):
                break
            # 못 가는 길이면 종료
            if arr[nr][nc] == 1:
                break

            if visited[nr][nc][dir] == 0:
                visited[nr][nc][dir] = visited[r][c][dir] + 1
                queue.append((nr, nc, dir))

        # Turn dir
        for nd in [1, 2, 3, 4]:
            if nd == dir:
                continue
            # 180도 회전인 경우 (상<->하, 좌<->우) => 2번 돌아야함
            if (dir == 1 and nd == 2) or (dir == 2 and nd == 1) or (dir == 3 and nd == 4) or (dir == 4 and nd == 3):
                turn = 2
            else:
                turn = 1
            if visited[r][c][nd] == 0:
                visited[r][c][nd] = visited[r][c][dir] + turn
                queue.append((r, c, nd))


# M : 세로 N : 가로 (M * N배열)
M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]

# 동서남북 : 1234

start_r,start_c,start_dir = map(int,input().split())
last_r,last_c,last_dir = map(int,input().split())

# 인덱스로 변환
start_r -= 1
start_c -= 1
last_r -= 1
last_c -= 1

# 방향 고려한 visited 3차원 배열
# 방향이 1~4로 되어있으니까 [0]*5
visited = [[[0]*5 for _ in range(N)] for _ in range(M)]
bfs()
