Q = [0] * 3
front = -1
rear = -1

def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(Q) == front

# 큐 맨 앞 원소를 반환
def Qpeek():
    if isEmpty():
        print('Queue Empty')
    else:
        return Q[(front+1)%len(Q)]

# 삽입
def enQueue(item):
    global rear
    if isFull():
        print('Queue Full')
    else:
        rear = (rear + 1) % len(Q)
        Q[rear] = item

# 앞 원소 가져오기
def deQueue():
    global front
    if isEmpty():
        print('Queue Empty')
    else:
        front = (front + 1) % len(Q)
        return Q[front]

enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
enQueue(5)
enQueue(6)
enQueue(7)
enQueue(8)
enQueue(9)
enQueue(10)
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())