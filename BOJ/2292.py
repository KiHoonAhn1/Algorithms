import sys

A = int(sys.stdin.readline())
count = 1
a = 0
b = 0
n = -1
while True:
    n += 1
    count += 1
    a = a + 6 * n
    b = b + 6 * (n + 1)
    if A == 1:
        print(1)
        break
    elif a + 2 <= A <= b + 1:
        print(count)
        break