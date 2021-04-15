import math
# input_text = '0269FAC9A0'
input_text = '0DEC'
num_byte = ''
for text in input_text:
    if ord(text) >= 65:
        num = ord(text) - 55
    else:
        num = int(text)

    for i in range(3, -1, -1):
        num_byte += "1" if num & (1 << i) else "0"

idx = len(num_byte)-1
pwd = []
while idx >= 6:
    if num_byte[idx] == '0':
        idx -= 1
    else:
        pwd.append(num_byte[idx-5:idx+1])
        idx -= 6

pwd = pwd[::-1]
bit_pwd = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
result = ''
for password in pwd:
    result += str(bit_pwd.index(password)) + ', '
print(result[:-2])