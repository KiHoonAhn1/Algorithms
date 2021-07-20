words = input()
num = 0
arr = ''
result = ''

for word in words:
    if ord(word) >= 65:
        arr += word
    else:
        num += int(word)

arr = sorted(arr)

for word in arr:
    result += word

result += str(num)

print(result)
