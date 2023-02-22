import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right] 

def sol_one(c):
    if c != '.':
        print(c, end='')
        sol_one(tree[c][0])
        sol_one(tree[c][1])
def sol_two(c):
    if c != '.':
        sol_two(tree[c][0])
        print(c, end='')
        sol_two(tree[c][1])
def sol_three(c):
    if c != '.':
        sol_three(tree[c][0])
        sol_three(tree[c][1])
        print(c, end='')
    
sol_one('A')
print()
sol_two('A')
print()
sol_three('A')