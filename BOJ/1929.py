import math

M, N = map(int, input().split())
for i in range(M, N+1):
    count = 0
    for j in range(1, int(math.floor(math.sqrt(i)))+1):
        if i % j == 0:
            count += 1
        if count > 1:
            continue
    if count == 1:
        print(i)