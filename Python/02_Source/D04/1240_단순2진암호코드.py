password = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111',
            '0111011', '0110111', '0001011']
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = ''
    pwd = []
    for i in range(N):
        a = input()
        if not arr and '1' in a:
            arr += a

    idx = M-1
    while idx >= 7:
        if arr[idx] == '0':
            idx -= 1
        else:
            pwd.append(arr[idx-6:idx+1])
            idx -= 7
    pwd = pwd[::-1]

    result = []
    for byte in pwd:
        result.append(password.index(byte))
    if ((result[0] + result[2] + result[4] + result[6]) * 3 + result[1] + result[3] + result[5] + result[7]) % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum(result)}')