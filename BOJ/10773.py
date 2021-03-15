import sys

N = int(sys.stdin.readline())
cog = []
result = 0
for _ in range(N):
    money = int(sys.stdin.readline())
    if money == 0:
        result -= cog.pop()
    else:
        result += money
        cog.append(money)
print(result)
