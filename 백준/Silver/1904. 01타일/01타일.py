from sys import stdin

input = stdin.readline

n = int(input())

tmp = [1,2]
for i in range(1, n):
    tmp = [tmp[1] % 15746, (tmp[0]+tmp[1])%15746]

print(tmp[0])