'''
5
2 3 1 2 2
'''

# 내 답
n = 5
stat = '2 3 1 2 2'
adventure = list(map(int, stat.split()))
adventure.sort()

group = []
cnt = 0
for i in adventure:
    if len(group) < i:
        group.append(i)
    if len(group) == i:
        cnt += 1
        group = []
        
print(cnt)

# 개선점
'''
굳이 append를 하며 시간을 잡아먹지 말고 count 변수로 계산해도 된다. 
'''