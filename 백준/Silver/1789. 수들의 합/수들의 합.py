import sys
input = sys.stdin.readline
s = int(input())
sum = 2
start = 1
while True:
    if start <= s:
        start += sum
        sum += 1
    else:
        print(sum-2)
        break