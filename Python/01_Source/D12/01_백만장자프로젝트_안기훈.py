T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    total = 0
    max_price = 0
    for i in range(2, N+1):
        if price[-i] < price[-i+1]:
            if max_price < price[-i+1]:
                max_price = price[-i+1]
            total += max_price - price[-i]
        else:
            if max_price > price[-i]:
                total += max_price - price[-i]
    print(f'#{tc} {total}')

    # while idx != N-1:
    #     max_price = 0
    #     for i in range(cnt ,N):
    #         if max_price < price[i]:
    #             max_price = price[i]
    #             idx = i
    #     total_price += max_price * (idx+1-cnt)
    #     if idx == cnt:
    #         break
    #     cnt = idx+1
    # for j in price[:cnt]:
    #     total_price -= j
    # if idx == 0:
    #     print(f'#{tc} 0')
    # else:
    #     print(f'#{tc} {total_price}')