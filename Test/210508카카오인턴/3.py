n = 8
k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
people = [i for i in range(n)]
idx = k
temp = []
answer = ''
for a in cmd:
    if len(a) > 1:
        dir, dis = a.split()
        dis = int(dis)
        if dir == "D":
            if idx + dis >= len(people):
                idx = (idx + dis) - len(people)
            else:
                idx += dis
        elif dir == "U":
            if idx - dis < 0:
                idx = len(people) + (idx - dis)
            else:
                idx -= dis
    else:
        if a == "C":
            temp.append(people.pop(idx))
            if idx == len(people):
                idx -= 1
        elif a == "Z":
            x = temp.pop()
            if x < people[0]:
                people.insert(x, 0)
                idx += 1
            elif x > people[-1]:
                people.append(x)
            else:
                for i in range(n-1):
                    if people[i] < people[i+1]:
                        people.insert(x, i+1)
                        if i+1 < idx:
                            idx += 1
                        break
for i in range(n):
    if i in temp:
        answer += 'X'
    else:
        answer += 'O'
print(answer)