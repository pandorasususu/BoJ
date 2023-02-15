from sys import stdin
import heapq
input = stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] * (v+1) for _ in range(v+1)]
distance = [float('inf')] * (v+1)
for _ in range(e):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

def sol(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dst, now = heapq.heappop(q)
        if distance[now] < dst:
            continue
        else:
            for i in graph[now]:
                value = dst + i[1]
                if distance[i[0]] > value:
                    distance[i[0]] = value
                    heapq.heappush(q, (value, i[0])) 
sol(k)

for i in range(1, v+1):
    if distance[i] == float('inf'):
        print('INF')
    else: print(distance[i])