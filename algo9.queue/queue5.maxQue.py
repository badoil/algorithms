import queue
from collections import deque

class MaxQueue:
  def __init__(self):
    self._data = queue.SimpleQueue()
    self._max = deque()

  def max(self):
    return self._max[0]

  def enqueue(self,val:int):
    self._data.put(val)
    while 0 < len(self._max) and self._max[-1] < val:
      self._max.pop()
    self._max.append(val)

  def dequeue(self):
    val = self._data.get()
    if val == self._max[0]:
      self._max.popleft()
    return val


##############################

class MaxQueue:
  def __init__(self):
    self._simpleQueue = queue.SimpleQueue()
    self._max = deque()

  def enque(self, val:int)-> None:
    self._simpleQueue.put(val)
    while len(self._max)>0 and self._max[-1] < val:
      self._max.pop()
    self._max.append(val)

  def deque(self) -> int:
    target = self._simpleQueue.get()
    if len(self._max)>0 and self._max[0] == target:
      self._max.popleft()
    return target

  def max(self) -> int:
    return self._max[0]
