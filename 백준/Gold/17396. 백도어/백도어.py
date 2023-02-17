import sys 
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
sight = list(map(int, input().split()))
sight[-1] = 0
graph = [[] for _ in range(n+1)]
total_time = [float('inf')] * (n+1)
total_time[0] = 0
for _ in range(m):
    a, b, t = map(int, input().split())
    if (sight[a] or sight[b]):
        continue    
    graph[a].append((b,t))
    graph[b].append((a,t))

q = []
heapq.heappush(q, (0, 0))
while q:
    now, time = heapq.heappop(q)
    if total_time[now] >= time:
        for i in graph[now]:
            next_time = time + i[1]
            if next_time < total_time[i[0]]:
                total_time[i[0]] = next_time
                heapq.heappush(q, (i[0], next_time))   

if total_time[n-1] == float('inf'): print(-1)
else: print(total_time[n-1])