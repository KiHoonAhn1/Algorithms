T = int(input())
for i in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    charge = [0]*(N+1+K)

    for j in station:
        charge[j] += 1
    charge[N] += 1

    count = 0
    a = 0
    while a < N:
        for k in range(K, 0, -1):
            if charge[a+k] == 1:
                if a+k >= N:
                    a += k
                    break
                charge[a+k] = 0
                a += k
                count += 1
                break
            if 1 not in charge[a:a+K+1]:
                count = 0
                break
            if a >= N:
                break
        if a >= N:
            break
        if count == 0:
            break
    print(f'#{i} {count}')
