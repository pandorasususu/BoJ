import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    graph = {i:[] for i in range(1, v + 1)}
    nodes = [0] * (v + 1)
    for __ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    isolated = []
    not_isolated = []
    for k in graph.keys():
        if graph[k] == []:
            isolated.append(k)
        else:
            not_isolated.append(k)
    q = deque()
    q += not_isolated
    nodes[not_isolated[0]] = 'r'
    ans = 'YES'
    ans_is_yes = True
    while q:
        now = q.popleft()
        if nodes[now] == 0:
            nodes[now] = 'r'
        for n in graph[now]:
            if nodes[n] == 0:
                if nodes[now] == 'r':
                    nodes[n] = 'b'
                else:
                    nodes[n] = 'r'
                q.appendleft(n)
            else:
                if nodes[now] == nodes[n]:
                    ans_is_yes = False
                    break
        if ans_is_yes == False:
            break
    if not ans_is_yes:
        ans = 'NO'
    print(ans)