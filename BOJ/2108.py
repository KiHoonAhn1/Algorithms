import sys
import statistics

N = int(sys.stdin.readline().rstrip())
arr = []
for t in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
# 정렬
arr.sort()

# 평균
tot = 0
for j in arr:
    tot += j
print(round(tot/N))

# 중앙값
print(arr[N//2])
a = statistics.multimode(arr)
# 최빈값
if len(a) >= 2: # 최빈값이 2개 이상이면
    print(a[1]) # 2번째로 작은 값 출력
else:
    print(a[0])

# 중간값
print(arr[N-1]-arr[0])
