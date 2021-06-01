numbers = [1, 1, 1, 1, 1]
target = 3
answer = 0

def getNum(numbers, now):
    global answer
    print(numbers, now)
    if len(numbers) == 1:
        if now + numbers[0] == target or now - numbers[0] == target:
            answer += 1
    else:
        getNum(numbers[1:], now+numbers[0])
        getNum(numbers[1:], now-numbers[0])

getNum(numbers, 0)

print(answer)

