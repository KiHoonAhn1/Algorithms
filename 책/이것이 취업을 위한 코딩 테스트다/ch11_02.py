'''
02984

567
'''

n1 = '02984'
n2 = '567'

result = int(n2[0])
for i in n2[1:]:
    if int(i) <= 1 or result <= 1:
        result += int(i)
    else:
        result *= int(i)
print(result)