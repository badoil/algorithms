# 싱글리 링크드 리스트를 이용해서 큐 구현하기
# 더블리 보다 메모리를 덜 쓰는 싱글리 링크드 리스트



class Node:
  def __init__(self,val: int):
    self.val = val
    self.next = None

class Queue:
  def __init__(self):
    self._head = Node(0)
    self._last = self._head

  def enqueue(self,val:int):
    new_node = Node(val)    
    self._last.next = new_node
    self._last = new_node

  def dequeue(self) -> int:
    if self._head == self._last:
      raise RuntimeError('No Elem')

    first_node = self._head.next
    value = first_node.val
    if first_node == self._last:
      self._last = self._head
      return value    
    
    self._head.next = first_node.next
    return value


queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(7)
queue.enqueue(9)

print(queue.dequeue(), end=' ')
print(queue.dequeue(), end=' ')
print(queue.dequeue(), end=' ')
print(queue.dequeue(), end=' ')
print(queue.dequeue(), end=' ')

# 1 3 5 7 9 




#################################################################



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
    value = firstNode.val
    if firstNode == self._last:
      self._last = self._head         # 하나 있는 것도 디큐 했으니 노드가 없는 상태로 만들어줌
      return value           

    secondNode = firstNode.right        
    self._head.next = secondNode        # 처음 노드 제외하고 두번째 노드를 처음 자리로 둔다

    return value