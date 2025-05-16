from collections import deque

N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in  range(N)]

# 상하좌우
di = [-1,1,0,0]
dj = [0,0,1,-1]

def bfs(r,c):
    q = deque()
    q.append((r,c))
    # 연합 국가 좌표
    cor = []
    cor.append((r,c))
    # 방문 처리
    visited[r][c] = 1
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni = i+di[d]
            nj = j+dj[d]
            # 범위 벗어나고 이미 방문했으면 통과
            if ni<0 or nj<0 or ni>=N or nj>=N or visited[ni][nj] ==1:
                continue
            # 조건에 맞으면
            # 1) 방문 처리 2) 큐에 넣어주고 3) 좌표에 추가
            if L<=(abs(arr[i][j] - arr[ni][nj])) <= R:
                visited[ni][nj] = 1
                q.append((ni,nj))
                cor.append((ni,nj))

    # 연합 국가 없으면 종료
    if len(cor) <= 1:
        return 0
    # 인구 이동
    people = sum(arr[a][b] for a,b in cor)
    change = people // len(cor)
    for x,y in cor:
        arr[x][y] = change
    return 1

# 이동 횟수
cnt = 0
while True:
    stop = 0
    visited = [ [0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                stop += bfs(r,c)
    # 종료 조건 (인구 이동이 없었다)
    if stop == 0:
        break
    cnt += 1

print(cnt)
