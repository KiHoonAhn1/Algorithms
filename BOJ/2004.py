n, m = map(int, input().split())
x, y = 1, 1
for i in range(m):
    x *= n
    x /= m
    n -= 1
    m -= 1

result = str(int(x//y))
print(len(result) - len(result.rstrip('0')))