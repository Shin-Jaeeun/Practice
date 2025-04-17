def solution(n, computers):

    # 그래프 생성
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 :
                graph[i+1].append(j+1)          # 노드 번호 = 인덱스 + 1

    def dfs(v):
        visited[v] = True

        for next in graph[v]:
            if not visited[next]:
                visited[next] = True
                dfs(next)

    answer = 0
    for n in range(1,n+1):
        for node in graph[n]:
            if not visited[node]:
                dfs(node)
                answer+=1

    return answer