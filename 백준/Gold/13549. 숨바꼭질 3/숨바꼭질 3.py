
from collections import deque
def bfs(N,K):
    queue = deque()
    queue.append(N)
    visit = [0] * 100001 # 최대크기 100000 / 최소시간 기록
    # 시작 점 방문 처리
    visit[N] = 1

    while queue:
        n = queue.popleft()
        # n*2는 시간 추가 안되니까 먼저 탐색 !!!
        if 0<=n*2<100001 and visit[n*2] == 0:
            visit[n*2] = visit[n]
            # 앞쪽에 추가
            queue.appendleft(n*2)

        for next in [n-1,n+1]:
            if 0<= next < 100001 and visit[next] == 0:
                visit[next] = visit[n] + 1 # 1초 증가
                queue.append(next)         # 뒤에 추가

    print(visit[K]-1)  #시작 1로 시작했으니까 -1해주기


N,K = map(int,input().split())
bfs(N,K)
