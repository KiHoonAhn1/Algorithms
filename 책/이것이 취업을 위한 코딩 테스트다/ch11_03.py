'''
0001100
'''

num = '0001100'
now = '999'
cnt = 0
for i in num:
    if now != i:
        now = i
        cnt += 1
print(cnt//2)