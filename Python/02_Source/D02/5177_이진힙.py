T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    tree = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        number = num_list[i-1]
        if num_list[i-1] < tree[i//2]:
            while i:
                if number < tree[i//2]:
                    tree[i], tree[i//2] = tree[i//2], number
                    i //= 2
                else:
                    break
        else:
            tree[i] = num_list[i-1]
    tot = 0
    while N:
        N //= 2
        tot += tree[N]
    print(f'#{tc} {tot}')