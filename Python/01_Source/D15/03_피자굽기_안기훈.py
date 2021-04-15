
def pizza(cheese_pizza):
    queue = []
    # 일단 화덕 크기 만큼 치즈피자를 넣는다
    for i in range(N):
        queue.append(cheese_pizza.pop(0))
    # 1개만 남은 상황이 아니라면
    while len(queue) != 1:
        # 1바퀴 돌았다고 가정하면, 치즈 반이 녹는다
        queue[0][0] = queue[0][0] // 2
        # 만약 치즈가 없다면
        if queue[0][0] == 0:
            if cheese_pizza:    # 화덕에 넣을 치즈피자가 더 남았다면
                queue.pop(0)    # 완성된 피자를 꺼내고,
                queue.append(cheese_pizza.pop(0)) # 새로운 치즈피자를 넣어주고
            else:
                queue.pop(0)    # 남은 피자가 더 없다면 꺼내기만 한다
        else:
            queue.append(queue.pop(0)) # 녹은 피자가 없다면 맨 뒤로 보낸다
    return queue[0][1]+1 # 인덱스보다 하나 더 큰 수가 피자의 순서이다.

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    cheese_pizza = []
    for i in range(M):
        cheese_pizza.append([cheese[i], i]) # 피자 순서를 함께 리스트에 넣어준다.
    print(f'#{tc} {pizza(cheese_pizza)}')