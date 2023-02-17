import sys 
from collections import deque
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
# graph = [[i - 1, i + 1, 2 * i] for i in range(100001)]
time_list = [float('inf')] * 1000001
q = deque()
q.append((0, n))
if n < k:
    while q:
        time, now = q.popleft()
        if n == 0 and now == 0:
            time_list[now] = 0
            # time_list[now+1] = 1 
            q.append((time+1, now+1))
            continue
        if now < 0:
            continue
        if now > k:
            if time_list[now] > time:
                time_list[now] = time
                q.append((time + 1, now - 1))
        elif now == k:
            if time_list[now] > time:
                time_list[now] = time
            continue
        else:
            if time_list[now] > time:
                time_list[now] = time
                q.appendleft((time, now * 2))
                q.append((time + 1, now + 1))
                q.append((time + 1, now - 1))

    # print(time_list[:k+1])
    print(time_list[k])
else:
    print(n-k)
    