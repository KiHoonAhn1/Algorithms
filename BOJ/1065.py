def hansoo(num):
    if num < 100:
        print(num)
    elif 100 <= num and num <= 1000:
        count = 99
        for i in range(100, num+1):
            if (int(str(i)[0]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[2])):
                count += 1
        print(count)
    elif len(str(num)) == 4:
        for i in range(100, 1000):
            if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
                count += 1
        else:
            if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]) and int(str(i)[1]) - int(str(i)[2]) == int(str(i)[2]) - int(str(i)[3]):
                count += 1
        print(count)

hansoo(int(input()))