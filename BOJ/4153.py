while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    if C >= A and C >= B:
        if A**2 + B**2 == C**2:
            print('right')
        else:
            print('wrong')
    if B >= A and B >= C:
        if A**2 + C**2 == B**2:
            print('right')
        else:
            print('wrong')
    if A >= B and A >= C:
        if B**2 + C**2 == A**2:
            print('right')
        else:
            print('wrong')
