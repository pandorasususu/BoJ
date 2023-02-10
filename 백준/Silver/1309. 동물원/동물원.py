from sys import stdin
input = stdin.readline

n = int(input())
one, two = 2, 1

for i in range(1, n):
    new_two = one + two
    new_one = new_two + two
    one, two = new_one, new_two

print((one + two) % 9901)