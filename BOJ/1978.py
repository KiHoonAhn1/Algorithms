N = int(input())
numbers = list(map(int, input().split()))
count_num = 0
for i in numbers:
    count = 0
    for j in range(1, i):
        if i % j == 0:
            count += 1
    if count == 1:
        count_num += 1
print(count_num)