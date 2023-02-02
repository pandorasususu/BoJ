from sys import stdin

input = stdin.readline

n = int(input())
cnt = 0
arr = []
def sol(total, start, end, middle):
    global cnt
    cnt += 1
    if total == 1:
        # arr.append([start, end])
        print(start, end)
        return
    
    sol(total-1, start, middle, end)
    # arr.append([start, end])
    print(start, end)
    sol(total-1, middle, end, start)

print(2**n-1)
sol(n, 1, 3, 2)
# print(cnt)
# for i in arr:
#     print(*i)



                