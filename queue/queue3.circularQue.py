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


###############################

class CircularQueue:
  def __init__(self, k: int):
    self._data = [None] * k
    self._rearIdx = -1
    self._frontIdx = 0
    self._size = k

  def enque(self, val: int):
    self.fullCheck()

    self._rearIdx += 1
    self._rearIdx = self._rearIdx % self._size
    self._data[self._rearIdx] = val
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