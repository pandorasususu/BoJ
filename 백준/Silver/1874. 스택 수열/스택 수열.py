import sys 
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
original = [i for i in range(1, n+1)]
stack = []
ans = ''
for i, v in enumerate(arr):
    if stack == [] or stack[-1] < v:
        while True:
            stack.append(original.pop(0))
            ans += '+'
            if stack[-1] == v:
                ans += '-'
                stack.pop()
                break
    else:    
        if stack[-1] == v:
            ans += '-'
            stack.pop()
        else:
            print('NO')
            break
else:
    print('\n'.join(ans))