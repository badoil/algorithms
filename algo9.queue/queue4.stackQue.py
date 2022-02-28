# 232
# 문제 :  Stack 2개를 이용하여 Queue를 구현하여라
# enqueue TC O(1), dequeue TC O(n)
# 이때 TC O(1) 인 디큐를 구현하라고 하면 armortized O(1)으로 구현해야함

# dequeue  op같은경우 O(1)이 필요한 경우와 O(n)이 필요한 경우 두가지 time complexity가 있는데 
# 그 때의 자료구조 상태에 따라서 O(1)이 필요한경우가 n번 나오게 되고 마지막에 O(n)이 필요한경우가 한번 나오게되서 이를 합해서 평균내면 분할상환 개념으로 O(1)이 필요했다 라고 볼 수 있음

class Queue:
  def __init__(self):
    self._pushStack = []
    self._popStack = []

  def enque(self, x: int) -> None:
    self._pushStack.append(x)

  def deque(self) -> int:
    if len(self._popStack) > 0:
      self._popStack.pop()

    self.moveToPopStack()
    return self._popStack.pop()


  def moveToPopStack(self):
    while self._pushStack:
      tempVal = self._pushStack.pop()
      self._popStack.append(tempVal)

queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(7)
print(queue.dequeue(), end= ' ')
print(queue.dequeue(), end= ' ')
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(6)
print(queue.dequeue(), end= ' ')
print(queue.dequeue(), end= ' ')
print(queue.dequeue(), end= ' ')
print(queue.dequeue(), end= ' ')
print(queue.dequeue(), end= ' ')


###################################################


class StackQueue:
  def __init__(self):
    self._pushStack = []
    self._popStack = []


  def stackEnqueue(self, val: int):
    self._pushStack.append(val)

  def stackDequeue(self) -> int:
    if len(self._popStack) > 0:
      return self._popStack.pop()

    self.movoToPopStack()

    return self._pushStack.pop()


  def movoToPopStack(self):
    while self._pushStack:
      val = self._pushStack.pop()
      self._popStack.append(val)