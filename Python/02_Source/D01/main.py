N = 13
data = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 6 9 6 10 6 11 7 12 11 13'

num_list = list(map(int, data.split()))

tree = [[0] * 3 for _ in range(N+1)]

parent = 0
for idx, number in enumerate(num_list):
    if idx % 2:
        # 자식노드
        child = number
        if not tree[parent][0]:
            tree[parent][0] = child # [0, 0, 0] => left 확인
        else:
            tree[parent][2] = child # [0, 0, 0] => right 확인
    else:
        # 부모노드 index
        parent = number

# tree 준비 끝!
print(tree)

# 전위 순회
def pre_order(node_index):
    if node_index:
        print(node_index, end=' ')
        pre_order(tree[node_index][0])
        pre_order(tree[node_index][2])

# 중위 순회
def in_order(node_index):
    if node_index:
        in_order(tree[node_index][0])
        print(node_index, end=' ')
        in_order(tree[node_index][2])

# 후위 순회
def post_order(node_index):
    if node_index:
        post_order(tree[node_index][0])
        post_order(tree[node_index][2])
        print(node_index, end=' ')

pre_order(1)
print()
in_order(1)
print()
post_order(1)