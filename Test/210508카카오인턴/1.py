num_dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def solution(s):
    print(s)
    answer = 0
    temp = ''
    for i in s:
        if 97 <= ord(i) <= 122:
            temp += i
        else:
            answer = answer * 10 + int(i)

        if len(temp) > 2 and temp in num_dict:
            answer = answer * 10 + num_dict[temp]
            temp = ''

    return answer