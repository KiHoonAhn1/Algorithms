def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 0:
        return 0
    else:
        return (paper(n-1) + paper(n-2)*2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N//10
    print(f'#{tc} {paper(n)}')