for i in range(4):
    N = list(map(int, input().split()))
    A = N[0:4]
    B = N[4:8]
    # A1, A2, A3, A4 = ~~ 끝날때 바꿔주자
    # A1 = [A[0], A[1]]
    # A2 = [A[2], A[3]]
    # A3 = [A[0], A[3]]
    # A4 = [A[2], A[1]]
    # B1 = [B[0], B[1]]
    # B2 = [B[2], B[3]]
    # B3 = [B[0], B[3]]
    # B4 = [B[2], B[1]]
    Ax = [A[0], A[2]]
    Ay = [A[1], A[3]]
    Bx = [B[0], B[2]]
    By = [B[1], B[3]]
    ## for 4
    for j in Ax:
        if j in Bx:
            for k in Ay:
                if By[0] < k < By[1]:
                    print('b')
                elif By[0] == k or By[1] == k:
                    print('c')

    for x in Ax:
        if Ax[0] == Bx[1] or Ax[1] == Bx[0]:
            Ay[0]

    # for 1
    if Ax[1] < Bx[0] or Ax[0] > Bx[1]:
        print('d')
        continue

    # for 2,3 -1, 3
    if Bx[0]<Ax[0]<Ax[1]<Bx[1] or Ax[0]<Bx[0]<Bx[1]<Ax[1]:
        if Ay[0]<By[0]<By[1]<Ay[1] or By[0]<Ay[0]<Ay[1]<By[1]:
            print('a')
            continue

    # for 2,3 -2
    if Bx[0]<Ax[0]<Bx[1] and By[0]<Ay[0]<By[1]:
        print('a')
        continue

    if Ax[0]<Bx[0]<Ax[1] and Ay[0]<By[0]<Ay[1]:
        print('a')
        continue
