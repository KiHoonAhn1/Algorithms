T = int(input())
for i in range(1, T+1):
    N = int(input())
    card = input()
    cards = []
    card_num = [0]*10
    for j in range(N):
        card_num[int(card[j])] += 1

    max_card = 0
    max_num = 0
    for k in range(10):
        if int(card_num[k]) > max_num:
            max_num = int(card_num[k])
            max_card = k
        elif int(card_num[k]) == max_num:
            max_card = k

    print(f'#{i} {max_card} {max_num}')