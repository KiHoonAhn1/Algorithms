# 중위 순회
for tc in range(1, 11):
    N = int(input())
    result = ''
    tree = [[0, '', 0] for _ in range(N+1)]
    for i in range(N):
        arr = list(input().split())
        for j in range(1, len(arr)):
            if j == 1:
                tree[int(arr[0])][1] = arr[1]
            elif j == 2:
                tree[int(arr[0])][0] = int(arr[j])
            else:
                tree[int(arr[0])][2] = int(arr[j])

    def in_order(node_index):
        global result
        if node_index:
            in_order(tree[node_index][0])
            result += tree[node_index][1]
            in_order(tree[node_index][2])

    in_order(1)
    print(f'#{tc} {result}')
