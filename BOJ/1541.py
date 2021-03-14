import sys

N = sys.stdin.readline().rstrip()
arr = list(N.split('-'))

num = []

for i in arr:
    num.append(list(map(int, (i.split('+')))))

result = 0
for j in range(len(num)):
    for k in num[j]:
        if j == 0:
            result += k
        else:
            result -= k
print(result)