arr = [-1, 2]
n = len(arr)
ans = False

for i in range(1<<n):
    result = []
    for j in range(n+1):
        if i & (1<<j):
            result.append(arr[j])
        # result 리스트 내에 있는 원소들을 더함
        total = 0
        for k in result:
            total += k
        # 공집합인 경우를 제외하고, total이 0이면 True
        if total == 0 and result != []:
            ans = True

print(ans)


