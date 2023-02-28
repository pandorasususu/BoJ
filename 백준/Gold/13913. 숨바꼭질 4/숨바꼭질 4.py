import sys
from collections import deque
input = sys.stdin.readline

s, e = map(int, input().split())
loc = [0] * 100001
from_array = [0] * 100001
def sol():
    if s < e:
        q = deque()
        q.append(s)
        while q:
            x = q.popleft()
            if x == e:
                print(loc[x])
                break

            for i in (x - 1, x + 1, x * 2):
                if 0 <= i <= 100000 and not loc[i]:
                    loc[i] = loc[x] + 1
                    from_array[i] = x
                    q.append(i)
        ans = deque()
        ans.appendleft(e)
        dest = e 
        while True:
            ans.appendleft(from_array[dest])
            dest = from_array[dest]
            if dest == s:
                break
        print(*ans)
    elif s == e:
        print(0)
        print(s)
    else:
        print(s - e)
        ans = [i for i in range(s, e - 1, -1)]
        print(*ans)
sol()