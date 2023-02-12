from sys import stdin
input = stdin.readline

def able(x):
    for i in range(x):
        if (row[i] == row[x]) or (abs(row[x] - row[i]) == abs(x-i)):
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if able(x):
                n_queens(x+1)
n = int(input())
row = [0] * n
ans = 0
n_queens(0)
print(ans)