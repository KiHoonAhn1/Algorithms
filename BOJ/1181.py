N = int(input())
arr = []
for _ in range(N):
    voca = input()
    arr.append([len(voca), voca])
arr.sort(key=lambda x: (x[0], x[1]))
print(arr[0][1])
for i in range(1, N):
    if arr[i][1] == arr[i-1][1]:
        continue
    else:
        print(arr[i][1])