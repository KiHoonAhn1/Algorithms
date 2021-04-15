N = int(input())
for i in range(N):
    big_box = 0
    boxes = int(input())
    box_list = list(map(int, input().split()))
    drop = 0
    for a in range(len(box_list)-1):
        if box_list[a] > box_list[a + 1]:
            big_box = box_list[a]
            final_drop = 0
            for b in box_list[a:]:
                if big_box > b:
                    final_drop += 1
            if drop < final_drop:
                drop = final_drop
    print(drop)