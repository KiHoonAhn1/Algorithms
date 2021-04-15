T = int(input())
for tc in range(1, T+1):
    # 노드의 개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    for i in range(N, 1, -1):
        if not i % 2 and i//2:
            if i == N:
                tree[i//2] = tree[i]
            else:
                tree[i//2] = tree[i] + tree[i+1]
    print(f'#{tc} {tree[L]}')