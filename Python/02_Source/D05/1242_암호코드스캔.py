password = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111',
            '0111011', '0110111', '0001011']

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    # 계산하기 편하게 필요없는 0 제거
    # 나중에 필요할지도 모름. len(word)가 14 이하인 경우에는 0을 포함시켜줘야 함
    for i in range(N):
        line = input()
        # 0만 있는 line 제거
        if ''.join(set(line)) == '0':
            continue
        # arr에 들어있지 않은 line만 추가한다
        if line not in arr:
            arr.append(line)
    # 양쪽 0부터 제거            
    for i in range(len(arr)):
        arr[i] = arr[i].strip('0')
    # arr 내에서 중복되는 line들 제거
    last_arr = []
    for _ in range(len(arr)):
        line = arr.pop(0)
        if not arr:
            last_arr.append(line)
        for j in arr:
            if line not in j:
                last_arr.append(line)
                break
        arr.append(line)