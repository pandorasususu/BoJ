from sys import stdin
import heapq
input = stdin.readline

            
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))

v1, v2 = map(int, input().split())
def sol(k):
    q = []
    heapq.heappush(q, (k, 0))
    distance[k] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        else:
            for i in graph[now]:
                cnd = dist + i[1]
                if cnd < distance[i[0]]:
                    distance[i[0]] = cnd
                    heapq.heappush(q, (i[0], cnd))

distance = [float('inf')] * (n+1)
distance_v1 = [float('inf')] * (n+1)
distance_v2 = [float('inf')] * (n+1)
sol(1)
first_distance = distance[:]
distance = [float('inf')] * (n+1)
sol(v1)
distance_v1 = distance[:]
distance = [float('inf')] * (n+1)
sol(v2)
distance_v2 = distance[:]

result = min(first_distance[v1] + distance_v1[v2] + distance_v2[n], first_distance[v2] + distance_v2[v1] + distance_v1[n])

if result == float('inf'):
    print(-1)
else: print(result)