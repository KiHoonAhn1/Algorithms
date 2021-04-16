def check(player, num):
    global winner
    for i in range(10):
        if player[i] >= 3:
            winner = num
            return
    for j in range(1, 9):
        if player[j - 1] >= 1 and player[j] >= 1 and player[j + 1] >= 1:
            winner = num
            return

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]
    winner = 0
    for idx, card in enumerate(cards):
        if idx % 2:
            player2[card] += 1
            check(player2, idx%2+1) if idx >= 5 else ''
        else:
            player1[card] += 1
            check(player1, idx%2+1) if idx >= 5 else ''
        if winner != 0:
            break
    print(f'#{tc} {winner}')