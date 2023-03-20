import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def sol():
    stack = []
    ans = [-1] * n
    for i in range(len(arr)-1, -1, -1):
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] 
        stack.append(arr[i])
    return ans

print(*sol())