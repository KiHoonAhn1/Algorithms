T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    fish = 0
    fish_arr = [0 for _ in range(11112)]
    for i in arr:
        fish_arr[i] -= 1
    for j in range(1, 11112):
        if not j % M:
            fish_arr[j] += K
        fish_arr[j] = fish_arr[j-1] + fish_arr[j]
    Possiblity = 'Possible'
    for k in fish_arr:
        if k < 0:
            Possiblity = 'Impossible'
            break

    print(f'#{tc} {Possiblity}')