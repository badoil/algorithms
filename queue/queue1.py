class QueueNode:
  def __init__(self,val: int):
    self.val = val
    self.left = None
    self.right = None

class Queue:
  def __init__(self):
    self._head = QueueNode(0)
    self._tail = QueueNode(0)
    self._head.right = self._tail
    self._tail.left = self._head

  def enqueue(self,val:int):
    new_node = QueueNode(val)    
    last_node = self._tail.left
    
    last_node.right = new_node
    new_node.left = last_node

    self._tail.left = new_node
    new_node.right = self._tail

  def dequeue(self) -> int:
    first_node = self._head.right
    if first_node == self._tail:
      raise RuntimeError('No Elem')

    value = first_node.val
    second_node = first_node.right
    self._head.right = second_node
    second_node.left = self._head

    return value


######################
class Queue:
  def __init__(self):
    self._headNode = QueueNode(-1)
    self._tailNode = QueueNode(-1)
    self._headNode.right = self._tailNode
    self._tailNode.left = self._headNode

  def enque(self, val: int):
    node = QueueNode(val)
    lastNode = self._tailNode.left
    lastNode.right = node
    node.left = lastNode
    node.right = self._tailNode
    self._tailNode.left = node

  def deque(self, val: int) -> int:
    firstNode = self._headNode.right
    if firstNode == self._tailNode:
      raise RuntimeError('no element')

    val = firstNode.val
    secondNode = firstNode.right
    self._headNode.right = secondNode
    secondNode.left = self._headNode

    return val