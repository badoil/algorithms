# 더블리 보다 메모리를 덜 쓰는 싱글리 링크드 리스트

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
    if self._head == self._last:        # 노드가 없는 경우
      raise RuntimeError('no element')

    firstNode = self._head.right        # 노드가 하나뿐인 경우
    if firstNode == self._last:
      self._head = self._last           # 하나 있는 것도 디큐 했으니 노드가 없는 상태로 만들어줌

    value = firstNode.val
    secondNode = firstNode.right        
    self._head.next = secondNode        # 처음 노드 제외하고 두번째 노드를 처음 자리로 둔다

    return value