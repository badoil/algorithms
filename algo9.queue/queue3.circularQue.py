# 622
# 문제 :   Circular Queue를 구현하여라
# 서큘러 큐를 배열로 구현

# 원형 큐는 실무에서도 많이 쓰임
# 원형큐는 용량이 제한되어 있어서 오버플로우가 일어날 수 있음
# 이를 리니어한 데이터 스트럭쳐로 구현해야함, 즉 array로
# 배열의 인덱스를 움직이면서 그에 해당하는 값을 넣어주거나(enquuee) 빼주어야함(dequeue)

# 인덱스가 배열의 길이를 넘어버리면 rearIdx가 다시 처음으로 돌아가야함
# 
# 이때 idx % len(array) 해줘야, 그 나머지 값으로 인덱스를 다시 찾아감


class CircularQueue:  
  def __init__(self, k: int):
    self._data = [None] * k
    self._rearIdx = -1
    self._frntIdx = 0
    self._size = 0

  def enQueue(self, value: int):
    self._fullCheck()
  
    self._rearIdx += 1
    self._rearIdx = self._rearIdx % len(self._data)
    self._data[self._rearIdx] = value
    self._size += 1


  def deQueue(self):
    self._emptyCheck()

    self._frntIdx +=1
    self._frntIdx = self._frntIdx % len(self._data)
    self._size -= 1
  

  def Rear(self) -> int:
    self._emptyCheck()
    return self._data[self._rearIdx]
    

  def Front(self) -> int:
    self._emptyCheck()
    return self._data[self._frntIdx]
  
  def _emptyCheck(self):
    if self._size == 0:
      raise RuntimeError('Queue is Empty')


  def _fullCheck(self):
    cap = len(self._data)
    if self._size == cap:
       raise RuntimeError('Queue is full')


circularQ = CircularQueue(4)
circularQ.enQueue(1)
circularQ.enQueue(3)
circularQ.enQueue(5)
circularQ.deQueue()
print(circularQ.Front(),circularQ.Rear())

# 3 5



###############################################################################



class CircularQueue:
  def __init__(self, k: int):
    self._data = [None] * k
    self._rearIdx = -1                              # 인덱스로만 원형큐의 값들을 관리함. 실제 self._data에 값이 있더라도 _rearIdx와 _frontIdx 범위 바깥이면 지워진거로 간주
    self._frontIdx = 0
    self._size = k

  def enque(self, val: int):
    self.fullCheck()

    self._rearIdx += 1                                # 엔큐는 끝에 원소가 들어가므로 rearIdx 체크
    self._rearIdx = self._rearIdx % self._size        # 인덱스가 배열의 길이를 넘어버리면 rearIdx가 다시 처음으로 돌아가야함
    self._data[self._rearIdx] = val                   # 만약 rearIdx가 길이를 넘었으면 rearIdx == size 이고 rearIdx는 0으로 들어감, 즉 앞에서 fullCheck 를 해주므로 rearIdx가 0이 비어있는 것
    self. _size -= 1

  def deque(self):
    self.emptyCheck()

    self._frontIdx += 1
    self._frontIdx = self._frontIdx % self._size
    self._size += 1


  def emptyCheck(self):
    if self._size == k:
      raise RuntimeError('empty')

    
  def fullCheck(self):
    if self._size == 0:
      raise RuntimeError('full')

  def rear(self):
    self.emptyCheck()
    return self._data[self._rearIdx]

  def front(self):
    self.emptyCheck()
    return self._data[self._frontIdx]