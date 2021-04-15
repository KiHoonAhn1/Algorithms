for tc in range(1, 11):
    T = int(input())
    arrays = []
    # 100x100 배열을 받아옴
    # arr = [list(map(int, input().split())) for _ in range(100)]
    for y in range(100):
        arr = list(map(int, input().split()))
        arrays.append(arr)


    max_num = 0
    # 행
    for i in range(len(arrays)):
        total = 0
        for j in arrays[i]:
            total += j
        if max_num < total:
            max_num = total
            
    # 열
    for i in range(len(arrays)):
        total = 0
        for j in range(len(arrays)):
            total += arrays[j][i]
        if max_num < total:
            max_num = total
            
    # 대각선 정방향
    total = 0
    for i in range(len(arrays)):
        total += arrays[i][i]
        if max_num < total:
            max_num = total

    # 대각선 역방향
    total = 0
    for i in range(1, len(arrays)+1):
        total += arrays[len(arrays)-i][len(arrays)-i]
        if max_num < total:
            max_num = total

    print(f'#{T} {max_num}')