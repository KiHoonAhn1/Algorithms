N = int(input())
for t in range(1, N+1):
    big_box = 0
    boxes = int(input())
    box_list = list(map(int, input().split()))
    drop = 0
    for a in range(boxes-1):
        if box_list[a] > box_list[a + 1]:
            big_box = box_list[a]
            final_drop = 0
            for b in box_list[a:]:
                if big_box > b:
                    final_drop += 1
            if drop < final_drop:
                drop = final_drop
    print(f'#{t} {drop}')