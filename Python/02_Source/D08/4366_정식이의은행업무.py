def num2oct(n, num):
    n = n[::-1]
    result = 0
    for i in range(len(n)):
        result += int(n[i]) * (num ** i)
    return result

T = int(input())
for tc in range(1, T+1):
    bin = list(input())
    ter = list(input())
    check = False
    ter_arr = ['0', '1', '2']
    for i in range(len(bin)):
        copy_bin = bin[::]
        copy_bin[i] = '1' if bin[i] == '0' else '0'
        bin2 = num2oct(copy_bin, 2)
        for j in range(len(ter)):
            copy_ter = ter[::]
            used_ter = [ter[j]]
            for k in ter_arr:
                if k not in used_ter:
                    used_ter.append(k)
                    copy_ter[j] = k
                    ter2 = num2oct(copy_ter, 3)
                    if ter2 == bin2:
                        check = True
                        break
            if check:
                break
        if check:
            break
    print(f'#{tc} {ter2}')

            # elif ter[i] == '2':
            #     ter[i] = '0'
            #     ter2 = num2oct(ter, 3)
            #     if ter2 == bin2:
            #         check = True
            #     ter[i] = '1'
            #     ter2 = num2oct(ter, 3)
            #     if ter2 == bin2:
            #         check = True

