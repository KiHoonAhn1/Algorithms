T = int(input())
for tc in range(T):
    N = int(input())
    wears = {}
    for n in range(N):
        wear, type = map(str, input().split())
        if type in wears:
            wears[type] += 1
        else:
            wears[type] = 1

    case = 1
    for i in wears.values():
        case *= i+1

    print(case-1)


