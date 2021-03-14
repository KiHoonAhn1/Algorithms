T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    if n >= m:
        b, s = n, m
    else:
        b, s = m, n

    b_result, s_result = 1, 1
    for i in range(s):
        b_result *= b
        b -= 1
    for j in range(s-1):
        s_result *= s
        s -= 1

    print(b_result//s_result)
