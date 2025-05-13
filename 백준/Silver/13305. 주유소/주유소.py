N = int(input())
road = list(map(int,input().split()))
cost = list(map(int,input().split()))
min_cost = cost[0]
result = 0

for i in range(N-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    result += road[i] * min_cost

print(result)