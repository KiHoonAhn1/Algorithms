C = int(input())
for i in range(C):
    scores = []
    scores = list(map(int, input().split()))
    total = 0
    for score in scores[1:]:
        total += score
    avg = total / scores[0]
    count = 0
    for score in scores[1:]:
        if score > avg:
            count += 1
    print('{0:0.3f}%'.format(round(count / scores[0] * 100, 3)))