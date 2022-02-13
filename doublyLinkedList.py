# 노코프
class ListNode:
  def __init__(self, key:int, val:int):
    self.key = key
    self.val = val
    self.left = None
    self.right = None

class LRUCache:
  def __init__(self, capacity: int):
    self._max_cap = capacity
    self._hashmap = {}
    self._list_head = ListNode(-1,-1)
    self._list_tail = ListNode(-1,-1)
    self._list_head.right = self._list_tail
    self._list_tail.left = self._list_head

  def get(self, key: int) -> int:
    value_node = self._hashmap.get(key)
    if value_node:
      self._removeFromList(value_node)
      self._addBack(value_node)
      val = value_node.val
      return val

    else:
      return -1

  def put(self, key: int, value: int) -> None:
    value_node = self._hashmap.get(key)
    if value_node:
      value_node.val = value
      self._removeFromList(value_node)
      self._addBack(value_node)
      return
    value_node = ListNode(key,value)
    self._addBack(value_node)
    self._hashmap[key] = value_node
    
    if self._max_cap<len(self._hashmap):
      lru_node = self._list_head.right
      lru_key = lru_node.key
      self._removeFromList(lru_node)
      self._hashmap.pop(lru_key)

  
  def _addBack(self, node:ListNode):
    tail_left = self._list_tail.left
    
    tail_left.right = node
    node.left = tail_left
    
    self._list_tail.left = node
    node.right = self._list_tail
    
    
  def _removeFromList(self,node:ListNode):
    left_node = node.left
    right_node = node.right

    left_node.right = right_node
    right_node.left = left_node


#오닐

class LRU:
  def __init__(self, cap:int):
    self._cap = cap
    self._hashTable = {}
    self._headNode = ListNode(-1, -1)
    self._tailNode = ListNode(-1, -1)
    self._headNode.right = self._tailNode
    self._tailNode.left = self._headNode


  def get(self, key: int) -> int:
    node = self._hashTable[key]
    if node:
      self._removeFromList(node)
      self._addToList(node)

      return node.val

    else:
      return -1

  def put(self, key:int, val:int) -> None:
    node = self._hashTable[key]
    if node:
      self._removeFromList(node)
      
      self._hashTable.pop(key)
      node.val = val
      self._hashTable[key] = node
      self._addToList(node)
      return

    newNode = ListNode(key, val)
    self._addToList(newNode)
    self._hashTable[key] = newNode

    if self._cap < len(self._hashTable):
      headRight = self._headNode.right
      headRightKey = headRight.key
      
      self._removeFromList(headRight)
      self._hashTable.pop(headRightKey)
      

  def _addToList(self, node: ListNode):
    leftTail = self._tailNode.left
    leftTail.right = node
    node.left = leftTail

    self._tailNode.left = node
    node.right = self._tailNode


  def _removeFromList(self, node: ListNode):
    leftNode = node.left
    rightNode = node.right

    leftNode.right = rightNode
    rightNode.left = leftNode