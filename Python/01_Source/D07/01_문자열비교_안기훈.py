T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt = 0
    for i in str2:
        for j in range(len(str1)):
            if str1[j + cnt] == i:
                cnt += 1
                break
            elif str1[j + cnt] != i:
                cnt = 0
                break
        if cnt == len(str1):
            break
    if cnt == len(str1):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
