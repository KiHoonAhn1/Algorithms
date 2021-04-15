T = int(input())

# 모든 N에 대한 경우의 수를 계산해놓기
l = [1, 1] # 0칸일 때 1, 1칸일떄 1, 초기값 설정
for i in range(2, 31):
    l.append(l[i-1] + 2 * l[i-2])

for tc in range(1, T+1):
    N = int(input()) // 10
    print("#{} {}".format(tc, l[N]))