hex2bin = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1],
}

table = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    data = [[] for _ in range(N)]

    # 입력을 받으면서 16진수를 2진수로 변형
    for i in range(N):
        row = input()
        for j in range(M):
            data[i].extend(hex2bin[row[j]])

    # data
    result = 0
    for i in range(N):
        # 16진수 가로 길이 M => 2진수 가로 길이 M * 4
        # 뒤에서 부터 탐색해서 1을 찾기위함!
        j = M * 4 - 1
        # 최소 가로 길이까지만!
        while j >= 55:
            # 1이 등장하고 (바로 윗 줄의 정보가 0일때 => 새로운 바코드 등장)
            if data[i][j] and data[i-1][j] == 0:
                # 글자 변환
                pwd = []
                for _ in range(8):
                    ratio3 = 0
                    ratio2 = 0
                    ratio1 = 0

                    # 1을 찾기 => 1이 등장하면 다음
                    while data[i][j] == 0:
                        j -= 1

                    # 1이 등장 => 마지막(1) 비율을 늘리고
                    while data[i][j] == 1:
                        ratio3 += 1
                        j -= 1

                    # 0이 등장 => 중간(0) 비율을 늘리고
                    while data[i][j] == 0:
                        ratio2 += 1
                        j -= 1

                    # 1이 등장 => 처음(1) 비율을 늘린다.
                    while data[i][j] == 1:
                        ratio1 += 1
                        j -= 1

                    # ratio1 : ratio2 : ratio3
                    MIN = min([ratio1, ratio2, ratio3])
                    # 숫자로 변환해서 담기
                    pwd.append(table[(ratio1 // MIN, ratio2 // MIN, ratio3 // MIN)])

                # 준비된 숫자가 유효한지 검사!
                pwd_sum = 0
                for pwd_idx, pwd_val in enumerate(pwd):
                    if pwd_idx % 2:
                        pwd_sum += pwd_val * 3
                    else:
                        pwd_sum += pwd_val

                if pwd_sum % 10 == 0:
                    result += sum(pwd)

            # 아니면 그냥 앞으로 이동한다
            else:
                j -= 1
    print('#{} {}'.format(tc, result))