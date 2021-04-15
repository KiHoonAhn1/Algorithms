def reward(n, cnt):
    global max_num
    money = int(''.join(map(str, nums)))
    if cnt == N:
        max_num = max(max_num, money)
        return
    for i in range(n, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] <= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                reward(i, cnt+1)
                nums[i], nums[j] = nums[j], nums[i]

T = int(input())
for tc in range(1, T+1):
    nums, N = map(int, input().split())
    nums = list(map(int, list(str(nums))))
    max_num = 0
    cnt = 0
    reward(0, cnt)
    if max_num == 0:
        while cnt != N:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            cnt += 1
        max_num = int(''.join(map(str, nums)))

    print(f'#{tc} {max_num}')

    # 1 321
    # 2 7732
    # 3 857147
    # 4 87664
    # 5 88832
    # 6 777770
    # 7 966354
    # 8 954311
    # 9 332211
    # 10 987645
    # for j in range(N):
    #     max_num = 0
    #     idx = 0
    #     overlap
    #     for k in range(j, len(num_arr)):
    #         if num_arr[k][1] >= max_num:
    #             max_num = num_arr[k][1]
    #             idx = num_arr[k][0]
    #     num_arr[j][1], num_arr[idx][1] = max_num, num_arr[j][1]
    #     print(tc, num_arr)
    # print(num_arr)