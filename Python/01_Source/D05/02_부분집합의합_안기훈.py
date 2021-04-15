T = int(input())
A = [q for q in range(1, 13)]
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1<<len(A)):
        arr = []
        for j in range(len(A)):
            if i & (1<<j):
                arr.append(A[j])
                if len(arr) > N:
                    break
        if len(arr) != N:
            continue
        tot = 0
        for a in arr:
            tot += a
        if len(arr) == N and tot == K:
            cnt += 1
    print(f'#{tc} {cnt}')
