T = int(input())
for i in range(1, T+1):
    # N명, M초, K개
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    result = 'Possible'
    fish = [0]*11112
    for k in customers:
        fish[k] += 1

    bread = 0
    for j in range(11112):
        if j > 0 and j % M == 0:
            bread += K

        bread -= fish[j]

        if bread < 0:
            result = 'Impossible'
            break

    print(f'#{i} {result}')