import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr_one = list(map(int, input().split()))
arr_two = list(map(int, input().split()))

print(*sorted(arr_one + arr_two))