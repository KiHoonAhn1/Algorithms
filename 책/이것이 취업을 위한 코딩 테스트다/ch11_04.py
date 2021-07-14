'''
5
3 2 1 1 9
'''

n = 5
coins = '3 2 1 1 9'
coinArr = list(map(int, coins.split()))
coinArr.sort()
getResult = False
result = 0
past = coinArr[0]
if coinArr[0] == 1:
    for coin in coinArr:
        if coin - past < 2:
            result += coin
            past = coin
        else:
            break
print(result + 1)
