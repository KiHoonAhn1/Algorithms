def make(idx, satisfaction, kcal):
    global result
    if kcal > L:
        return
    if idx == N:
        if satisfaction > result:
            result = satisfaction
        return

    make(idx+1, satisfaction, kcal)
    make(idx+1, satisfaction+ingredients[idx][0], kcal+ingredients[idx][1])


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    ingredients = []
    result = 0
    for i in range(N):
        score, kcal = map(int, input().split())
        ingredients.append([score, kcal])

    make(0, 0, 0)
    print(f'#{tc} {result}')