Q = [0] * 3
front = -1
rear = -1

def isEmpty():
    return front == rear

def isFull():
    return rear == len(Q) - 1

# 큐 맨 앞 원소를 반환
def Qpeek():
    if isEmpty():
        print('Queue Empty')
    else:
        return Q[front+1]

# 삽입
def enQueue(item):
    global rear
    if isFull():
        print('Queue Full')
    else:
        rear = rear + 1
        Q[rear] = item

# 앞 원소 가져오기
def deQueue():
    global front
    if isEmpty():
        print('Queue Empty')
    else:
        front = front + 1
        return Q[front]

enQueue(1)
enQueue(2)
enQueue(3)
print(f'{deQueue(), deQueue(), deQueue()}')