def stars(N, x, y):
    # a = '***\n* *\n***\n'
    if N==1:
        star[y][x] = '*'
    else:
        N = N // 3
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    stars(N, x + j * N, y + i * N)

N = int(input())
star = [[' ' for _ in range(N)] for _ in range(N)]
stars(N, 0, 0)
for k in star:
    print(''.join(k))