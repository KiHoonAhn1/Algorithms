def binary(P, goal):
    a = 1
    c = int((a + P) / 2)
    cnt = 1
    while True:
        cnt += 1
        if c > goal:
            P = c
            c = int((a + P) / 2)
        elif c < goal:
            a = c
            c = int((a + P) / 2)
        else:
            return cnt


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    Pa = binary(P, A)
    Pb = binary(P, B)
    if Pa < Pb:
        print(f'#{tc} A')
    elif Pa == Pb:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')
