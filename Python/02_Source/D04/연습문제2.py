import math
input_text = '0F97A3'
num_byte = ''
for text in input_text:
    if ord(text) >= 65:
        num = ord(text) - 55
    else:
        num = int(text)

    for i in range(3, -1, -1):
        num_byte += "1" if num & (1 << i) else "0"

answer = [0 for _ in range(math.ceil(len(num_byte) / 7))]
for i in range(math.ceil(len(num_byte) / 7)):
    result = 0
    if i == math.ceil(len(num_byte) / 7)-1 and len(num_byte[i*7:]) % 7:
        for j in range(len(num_byte[i*7:])):
            result += int(num_byte[7*i+j]) * (1 << (len(num_byte[i*7:])-1-j))
        answer[i] = result
    else:
        for j in range(7):
            result += int(num_byte[7 * i + j]) * (1 << (6 - j))
        answer[i] = result

print(answer)