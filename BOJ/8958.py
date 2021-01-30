N = int(input())
for i in range(N):
    M = input()
    total_score = 0
    score = 0
    for i in range(0, len(M)):
        if M[i] == 'O':
            score += 1
            total_score += score
        else:
            score = 0
    print(total_score)