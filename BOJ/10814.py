T = int(input())
arr = []
for tc in range(T):
    age, name = map(str, input().split())
    age = int(age)
    arr.append([age, name])

for i in arr:
    i[0] == int(i[0])
arr.sort(key=lambda x:x[0])

for j in arr:
    print(j[0], j[1])