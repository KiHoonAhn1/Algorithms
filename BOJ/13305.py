import sys
N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
fuel = list(map(int, sys.stdin.readline().split()))

minFuel = 1000000000
result = 0
for i in range(N-1):
    if fuel[i] < minFuel:
        minFuel = fuel[i]
    result += minFuel * distance[i]

print(result)