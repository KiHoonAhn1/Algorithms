N, K = map(int, input().split())
arr = []
for money in range(N):
    arr.append(int(input()))
arr = sorted(arr, reverse=True)
cnt = 0
tot = 0
for i in arr:
    cnt += K // i
    K = K % i
    if K == 0:
        break
print(cnt)