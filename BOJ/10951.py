A = int(input())
B = int(input())
C = int(input())

for i in range(0, 10):
    count = 0
    for a in str(A * B * C):
        if i == int(a):
            count += 1
    print(count)