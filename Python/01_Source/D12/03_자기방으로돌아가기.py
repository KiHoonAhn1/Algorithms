T = int(input())
for tc in range(1, T+1):
    arr = [0] * 201
    N = int(input())
    for i in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        s = (s+1) // 2
        e = (e+1) // 2
        for j in range(s, e+1):
            arr[j] += 1

    max_minutes = 0
    for k in arr:
        if max_minutes < k:
            max_minutes = k
    print(f'#{tc} {max_minutes}')