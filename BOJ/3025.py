listSet = set()
for i in range(10):
    a = int(input())
    listSet.add(a % 42)
print(len(listSet))