# deque 는 doubly ended queue 라고 해서, 양쪽 끝 모두 인&아웃을 지원(append, appendleft, pop, popleft)
# 즉 이 문제에서는 맥스큐를 디큐 사용하고, 직접 구현하지는 않음

# queue.SimpleQueue() 는 말 그대로 FIFO 인 심플한 큐
# deque 는 양쪽에서 인앤아웃 가능

# max(): O(1), dequeue: O(1)
# enqueue: amortized O(1), maxQueue에서 이미 들어있는 값과 새로운 값을 비교해야 하기 대문에 worst case 인 경우, O(n)인 경우도 있을 수 있지만
# 분할 상환으루다가 amortized O(1)

# 종류가 다른 두개의 큐를 사용하여 현재 큐의 최대값을 맥스큐에 넣어두는 것임
# 이때 맥스큐는 내림차순으로 정렬되어 있다고 생각, 즉 deque[0]이 제일 큰 수임
# 디큐 값이 deque[0] 와 같으면 맥스큐도 popleft 해줌
# 다만 인큐할때 새로운 값이 기존의 값보다 큰 경우, 맥스큐에 오른쪽에 있는 기존 값들을 다 팝하고 새 값을 넣어줘야함, 맥스큐에는 새로넣을 값보다 작은 값은 있을 필요가 없기 때문임
# 이때 맥스큐의 기존값을 지우기 위해서는 오른쪽에서 팝을 해줘야함. 이는 일반적인 큐로는 불가능, 그래서 맥스큐는 양쪽에서 팝(pop, popleft) 모두 되는 deque를 쓴것임

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


######################################


class QueueMax:
  def __init__(self):   
    self._queue = queue.SimpleQueue()     # FIFO
    self._max = deque()                   # 양쪽 끝 모두 인&아웃을 지원(append, appendleft, pop, popleft)

  def dequeue(self):
    val = self._queue.get()           # 처음 들어간 왼쪽 값 디큐
    if val == self._max[0] :          # 이 값이 현재 이 큐의 맥스값이라면 맥스큐에서도 팝 레프트
      self._max.popleft()
    return val

  def enqueue(self, val):
    self._queue.put(val)                                 # 나중에 들어간 오른쪽 값 인큐
    while len(self._max) > 0 and val > self._max[-1]:    # 맥스큐에 오른쪽 값들이 새로 넣을 값보다 작으면 그 값들을 오른쪽에서 빼줌
      self._max.pop()               # 맥스큐에는 새로넣을 값보다 작은 값은 있을 필요가 없기 때문

    self._max.append(val)           # 그리고 새로운 값을 오른쪽에서 넣어줌
                                    # 이렇게 되면 맥스큐에는 향상 제일 큰 수는 맨 왠쪽에, 그리고 내림 차순으로 정렬됨
  def maxQueue(self):
    return self._max[0]