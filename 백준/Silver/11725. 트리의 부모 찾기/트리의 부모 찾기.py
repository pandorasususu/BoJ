import sys
input = sys.stdin.readline

n = int(input())
graph = {i: [] for i in range(1, n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [0] * (n+1)
stack = [1]
while stack:
    current_node = stack.pop()
    for i in graph[current_node]:
        if parent[i] == 0:
            parent[i] = str(current_node)
            stack.append(i)
print('\n'.join(parent[2:]))