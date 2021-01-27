h, m = map(int, input().split())
if m-45 < 0:
    if h == 0:
        h = 23
        m = m + 15
    else:
        h = h - 1
        m = m + 15
    print(f'{h} {m}')
else:
    m = m - 45
    print(f'{h} {m}')