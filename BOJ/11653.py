N = int(input())
while True:
    for i in range(2, N+1):
        if N % i == 0:
            N //= i
            print(i)
            if N == 1:
                break
            else:
                break
    if N == 1:
        break