M = int(input())
N = int(input())
number_sum = 0
number_min = N
for i in range(M, N+1):
    count = 0
    for j in range(1, i+1):
        if count > 2:
            continue
        if i % j == 0:
            count += 1
    if count == 2:
        number_sum += i
        if number_min > i:
            number_min = i
if number_sum == 0:
    print(-1)
else:
    print(number_sum)
    print(number_min)