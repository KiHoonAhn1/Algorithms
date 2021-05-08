dx = [1, 0, -1]
dy = [0, -1, 0]

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
def check(x, y, distance):
    for i in range(3):
        if distance >= 2:
            return True
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if place[nx][ny] == 'X':
                continue
            elif place[nx][ny] == 'O':
                check(nx, ny, distance+1)
            else:
                if a != nx or b != ny:
                    return False
    return True

answer = []
for place in places:
    mask = True
    for x in range(5):
        for y in range(5):
            if place[x][y] == "P":
                a, b = x, y
                if not check(x, y, 0):
                    mask = False
                    break
        if not mask:
            break
    if mask:
        answer.append(1)
    else:
        answer.append(0)
print(answer)



