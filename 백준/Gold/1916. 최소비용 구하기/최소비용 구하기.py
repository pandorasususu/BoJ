from sys import stdin
import heapq
input = stdin.readline

            
n, m = int(input()), int(input())
graph = [[] for _ in range(n+1)]
# print(graph)
for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
# print(graph)
s, e = map(int, input().split())
distance = [float('inf')] * (n+1)
def sol(k):
    q = []
    heapq.heappush(q, (s, 0))
    distance[s] = 0

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

sol(s)
# print(graph)
print(distance[e])