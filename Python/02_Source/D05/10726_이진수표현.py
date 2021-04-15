T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    switch = 'ON'
    num_byte = ''
    for i in range(N-1, -1, -1):
        num_byte += '1' if M & (1 << i) else '0'

    for j in num_byte:
        if j == '0':
            switch = 'OFF'

    print(f'#{tc} {switch}')