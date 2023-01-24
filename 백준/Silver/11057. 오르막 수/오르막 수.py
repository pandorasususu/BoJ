import sys
input = sys.stdin.readline

mod = 10007
dict = {i: [0] * 10 for i in range(1, 1001)}
dict[1] = [10]
for i in range(2, 1001):
    for j in range(10):
        if i == 2:
            dict[i][j] = j+1
        elif j == 0:
            dict[i][j] = 1
        else:
            dict[i][j] = dict[i][j-1] + dict[i-1][j]
n = int(input())
print(sum(dict[n])%mod)