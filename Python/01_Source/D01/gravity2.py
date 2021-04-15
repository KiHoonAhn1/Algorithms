T = int(input()) # input: 한 줄 읽어 # int : 정수형으로 형변환
for tc in range(1, T+1):
    # 입력
    N = int(input)
    boxTop = input().split()
    room = [[0 for _ in range(100)] for _ in range(N)]
    for i in range(N):
        for j in range(boxTop[i]):
            room[i][j] = 1
    # 계산
    Max = 0 # 최대 낙차 저장
    for i in range(N): # 각 행마다
        if boxTop[i] > 0:
            dist = 0
            for j in range(i+1, N):
                if room[j][boxTop[i] - 1] == 0:
                    dist += 1
            if Max < dist:
                Max = dist
    # 출력
    print(f'#{tc} {Max}')