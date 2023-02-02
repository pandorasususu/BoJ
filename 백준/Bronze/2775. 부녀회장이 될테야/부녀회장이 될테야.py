from sys import stdin

input = stdin.readline

arr = [[i for i in range(15)]] + [[0] * 15 for i in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        arr[i][j] = sum(arr[i-1][1:j+1])

t = int(input())

for _ in range(t):
    f, r = int(input()), int(input())
    print(arr[f][r])