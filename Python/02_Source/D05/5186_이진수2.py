T = int(input())
for tc in range(1, T+1):
    N = float(input())
    num_byte = ''
    cnt = 0
    overflow = False
    while N or cnt < 13:
        cnt += 1
        N *= 2
        if N >= 1:
            N -= 1
            num_byte += '1'
        else:
            num_byte += '0'

    if cnt == 13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {num_byte}')