def password(arr):
    while True:
        for i in range(1, 6):
            q = arr.pop(0) - i
            if q <= 0:
                q = 0
                arr.append(q)
                return arr
            else:
                arr.append(q)

for _ in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{N} {" ".join(map(str, password(arr)))}')
