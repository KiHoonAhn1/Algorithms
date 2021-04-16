def tower(n, height): # n은 index
    global min_height
    if n == N:
        if height >= B:
            min_height = min(min_height, height)
        return
    tower(n+1, height+clerks[n])
    tower(n+1, height)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    clerks = list(map(int, input().split()))
    min_height = 987654321
    tower(0, 0)
    print(f'#{tc} {min_height - B}')