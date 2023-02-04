from sys import stdin
input = stdin.readline

n = int(input())

def sol(arr):
    if len(arr) == n:
        print(*arr)
        return
    for i in range(1, n+1):
        if i not in arr:
            sol(arr + [i])

sol([])