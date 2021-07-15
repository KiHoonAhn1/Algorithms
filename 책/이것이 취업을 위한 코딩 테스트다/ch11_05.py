'''
5 3
1 3 2 3 2
'''
n, m = 5, 3
n1, m1 = 8, 5

array = '1 3 2 3 2'
array1 = '1 5 4 3 2 4 5 2'

ballArr = [0] * 11

balls = list(map(int, array.split()))
for i in balls:
    ballArr[i] += 1

result = 0
for i in range(m1):
    n1 -= ballArr[i]
    result += ballArr[i] * n1

print(result)