T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    num_list = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E+2)]

    parent = 0
    for idx, number in enumerate(num_list):
        if idx % 2:
            child = number
            if not tree[parent][0]:
                tree[parent][0] = child
            else:
                tree[parent][2] = child
        else:
            parent = number

    cnt = 0
    def pre_order(node_index):
        global cnt
        if node_index:
            cnt += 1
            pre_order(tree[node_index][0])
            pre_order(tree[node_index][2])

    pre_order(N)
    print(f'#{tc} {cnt}')