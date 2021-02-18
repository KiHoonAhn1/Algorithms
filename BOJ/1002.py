T = int(input())
for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    rm = abs(r2 - r1)
    # 같은 위치에 있는 경우 무한
    if d == 0:
        if r1 == r2:
            print(-1)
        # 원 안에 접하지 않는 원
        elif r1 != r2:
            print(0)
    else:
        if r1+r2 > d:
            # 원 안에 원
            if rm == d:
                print(1)
            elif rm > d:
                print(0)
            else:
                print(2)
        # 외접
        elif r1+r2 == d:
            print(1)
        # 밖에서 아예 접하지 않을 때
        elif r1+r2 < d:
            print(0)
        else:
            print(0)