import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def sol():
    ans = 0
    one = set()
    for _ in range(n):
        one.add(input())
        # word = input()
        # one[word] = True
    for _ in range(m):
        word = input()
        if word in one:
            ans += 1
    return ans

print(sol())