T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    result = A*B
    remain = 0
    while True:
        remain = A % B
        if remain == 0:
            break
        A = B
        B = remain
    print(round(result/B))