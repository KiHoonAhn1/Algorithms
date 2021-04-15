T = int(input())
for tc in range(1, T+1):
    A = input()
    stick = 0
    sticks = 0
    cnt = 0
    for i in range(len(A) - 1):
        if A[i] == '(' and A[i+1] == '(':
            sticks += 1
            stick += 1

        elif A[i] == ')' and A[i+1] == ')':
            stick -= 1

        elif A[i] == '(' and A[i+1] == ')':
            sticks += stick

    print(f'#{tc} {sticks}')