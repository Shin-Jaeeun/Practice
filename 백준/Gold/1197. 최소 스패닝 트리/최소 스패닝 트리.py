import heapq, sys
input = sys.stdin.readline

def prim(start_node):
    pq = [ (0,start_node) ]  #(비용,노드)
    key = [float('inf')] * (V+1)
    visited = [False] * (V+1)
    min_weight = 0
    key[start_node] = 0
    count = 0

    while pq and count < V :
        weight,node = heapq.heappop(pq)

        # 이미 방문한 노드면 패스
        if visited[node] :
            continue

        visited[node] = True
        min_weight += weight
        count += 1

        for next_node, cost in graph[node]:
            if not visited[next_node] and cost<key[next_node]:
                key[next_node] = cost
                heapq.heappush(pq,(cost,next_node))

    return min_weight

# V : 정점 개수 / E : 간선 개수
V,E = map(int,input().split())
graph = [ [] for _ in range(V+1) ]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

print(prim(1))