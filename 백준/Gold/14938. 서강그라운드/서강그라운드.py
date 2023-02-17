import sys 
import heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    if l <= m:
        graph[a].append((b, l))
        graph[b].append((a, l))
visited = [[0] * (n+1) for _ in range(n+1)]
max_items = 0
for i in range(1, n+1):
    q = [(i, 0)]
    visited[i][i] = items[i]
    while q:
        now, now_len = q.pop(0)
        for g in graph[now]:
             if now_len + g[1] > m:
                continue
            #  if visited[i][now] != 0 and now != i:
            #     continue
             else:
                 visited[i][g[0]] = items[g[0]]
                 q.append((g[0], now_len + g[1]))
    if max_items < sum(visited[i]):
        max_items = sum(visited[i])
# print(visited)
print(max_items)
