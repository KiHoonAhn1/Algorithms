N, M = map(int, input().split())
arr = list(map(int, input().split()))
maxTot = 0
end = 0
tot = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tot = arr[i] + arr[j] + arr[k]
            if tot <= M and tot > maxTot:
                maxTot = tot
print(maxTot)
