###########

class QueueNode:
  def __init__(self, val: int):
    self.val = val
    self.next = None

class singlyQue:
  def __init__(self):
    self._head = QueueNode(-1)
    self._last = self._head

  def enque(self, val:int) -> None:
    node = QueueNode(val)
    self._last.next = node
    self._last = node

  def deque(self) -> int:
    if self._head == self._last:
      raise RuntimeError('no element')

    firstNode = self._head.right
    if firstNode == self._last:
      self._head = self._last

    value = firstNode.val
    secondNode = firstNode.right
    self._head.next = secondNode

    return value