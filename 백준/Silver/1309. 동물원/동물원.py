from sys import stdin
input = stdin.readline

n = int(input())
one, two = 2, 1
for i in range(1, n):
    # one, two = (one + 2 * two) % 9901 , (one + two) % 9901
    one, two = (one + 2 * two) % 9901 , (one + two) % 9901

# print(one + two)
print((one + two)%9901)