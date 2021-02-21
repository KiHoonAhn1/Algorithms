N = int(input())
result = 666
cnt = 0
while True:
    if '666' in str(result):
        cnt += 1
    if cnt == N:
        print(result)
        break
    result += 1
    
    # 시간 초과로 실패
# for i in range(3000000):
#     cnt = 0
#     for j in range(len(str(i))):
#         if str(i)[j] == '6':
#             cnt += 1
#         elif str(i)[j] != '6':
#             cnt = 0
#         if cnt == 3:
#             break
#     if cnt == 3:
#         result += 1
#     if result == N:
#         print(i)
#         break