def in_order(n):
    if len(tree[n]) > 1:
        a = in_order(tree[n][0])
        b = in_order(tree[n][2])
        if tree[n][1] == '*':
            return a * b
        elif tree[n][1] == '+':
            return a + b
        elif tree[n][1] == '-':
            return a - b
        elif tree[n][1] == '/':
            return a / b
    else:
        return tree[n][0]

for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for i in range(N):
        num = list(input().split())
        for x in range(len(num)):
            if num[x] == '+' or num[x] == '-' or num[x] == '/' or num[x] == '*':
                continue
            else:
                num[x] = int(num[x])
        for j in range(len(num)):
            if j == 1:
                tree[num[0]].insert(1, num[j])
            elif j == 2:
                tree[num[0]].insert(0, num[j])
            elif j == 3:
                tree[num[0]].insert(2, num[j])
    print(f'#{tc} {int(in_order(1))}')
