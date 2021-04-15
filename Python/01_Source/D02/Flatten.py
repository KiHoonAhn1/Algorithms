for a in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    count = 0
    while dump != count:
        h_box = 0
        h_box_loc = 0
        l_box = 100
        l_box_loc = 0
        for i in range(len(boxes)):
            if boxes[i] > h_box:
                h_box = boxes[i]
                h_box_loc = i
            if boxes[i] < l_box:
                l_box = boxes[i]
                l_box_loc = i
        boxes[h_box_loc] -= 1
        boxes[l_box_loc] += 1
        count += 1
    final_h = 0
    final_l = 100
    for j in range(len(boxes)):
        if boxes[j] > final_h:
            final_h = boxes[j]
        if boxes[j] < final_l:
            final_l = boxes[j]
    print(f'#{a} {final_h - final_l}')
