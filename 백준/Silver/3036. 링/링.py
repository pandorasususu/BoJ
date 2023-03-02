import sys
# from collections import deque
# import random
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    a, b = arr[0], arr[i]
    div = 2
    while True:
        if a % div == 0 and b % div == 0:
            a //= div
            b //= div
        else:
            div += 1
        if (a == 1 or b == 1) or (div > a or div > b):
            print(f'{a}/{b}')
            break