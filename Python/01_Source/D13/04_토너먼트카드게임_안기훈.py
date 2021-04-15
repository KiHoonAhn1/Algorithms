def find(l, r): # l : 카드의 왼쪽 끝, r : 카드의 오른쪽 끝
    if l == r:# 카드가 한 장? 호출 그만해.
        return l
    # 절반씩 나누기 위해 재귀 호출
    result1 = find(l, (l+r)//2) #왼쪽
    result2 = find((l+r)//2+1, r) # 오른쪽
    if card[result1] == card[result2]:
        return result1
    # 가위 1, 바위 2, 보 3
    else:
        if card[result1] ==1 and  card[result2] == 2:
            #바위가 이김 => 2 승
            return result2
        elif card[result1] == 1 and card[result2] == 3:
            return result1
        elif card[result1] == 2 and card[result2] == 1:
            return result1
        elif card[result1] == 2 and card[result2] == 3:
            return result2
        elif card[result1] == 3 and card[result2] == 1:
            return result2
        elif card[result1] == 3 and card[result2] == 2:
            return result1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))
    print("#{} {}".format(tc,find(1,N)))