import sys 
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
arr = input().split()
one, two = set(), set()
for i, v in enumerate(arr):
    if v in ['a','e','i','o','u']:
        one.add(v)
    else:
        two.add(v)
comb = set()

for i in range(1, l - 1):
    tmp_one = [*combinations(one, i)]
    for v1 in tmp_one:
        tmp_two = [*combinations(two, l - i)]
        for v2 in tmp_two:
            comb.add(''.join(sorted(v1+v2)))
print('\n'.join(sorted(list(comb))))