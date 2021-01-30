while True:
    try:
        A, B, C = map(int, input().split())
        for i in range(0, 10):
            print(str(A*B*C).count(i))
    except:
        break