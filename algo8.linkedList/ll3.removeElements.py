# 203 
# remove linked list elements
# 지우고자 하는 val을 갖는 모든 엘리먼트 삭제하기

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []
 
# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50


from typing import List

class NodeList:
  def __init__(self, val):
    self.val = val
    self.next = None

def createNodeList(inList: List[int]) -> NodeList:
  if len(inList) == 0:
    raise RuntimeError('empty list')

  headNode = NodeList(inList[0])
  lastNode = headNode

  for idx in range(1, len(inList)):
    node = NodeList(inList[idx])
    lastNode.next = node
    lastNode = node

  return headNode

def printNodes(node: NodeList):
  crtNode = node
  while crtNode is not None:
    print(crtNode.val, end=" ")
    crtNode= crtNode.next


class ElementRemover:
  def __init__(self,val):
    self.__val = val

  #arg_node data is not kept
  def recursive(self, node: NodeList) -> NodeList:
    if not node:
      return None
    next_node = self.recursive(node.next)
    if node.val == self.__val:
      return next_node
    else:
      node.next = next_node
      return node
  
  #arg_node data is not kept
  def iterative(self, node: NodeList) -> NodeList:    
    dummy_head = NodeList(0)
    dummy_head.next = node
    
    crnt_node = node
    prev_node = dummy_head
    while crnt_node:
      if crnt_node.val == self.__val:
        prev_node.next = crnt_node.next
        crnt_node = crnt_node.next
      else:
        crnt_node = crnt_node.next
        prev_node = prev_node.next
    return dummy_head.next
  
head = createNodeList([1,3,5,7,3,1])
printNodes(head)

remover = ElementRemover(1)
ret = remover.recursive(head)
printNodes(ret)




#####################################################################################



class RemoveElements:
  def __init__(self, val):        # 지우고 싶은 노드의 밸류가 객체를 생성할 때 생성자로 들어옴
    self._val = val

  def _recurRemove(self, node: NodeList) -> NodeList:   # 재귀적인 방법은 더미노드가 필요없음
    if not node:    # 종료조건
      return None
    
    nextNode = self._recurRemove(node.next)

    if node.val == self._val:
      return nextNode
    else:
      node.next = nextNode
      return node

  def _iterRemove(self, node: NodeList) -> NodeList:  # 반복문은 더미노드 필요함
    dummyNode = NodeList(0)
    dummyNode.next = node

    crtNode = node
    prevNode = dummyNode
    while crtNode is not None:
      if crtNode.val == self._val:
        prevNode.next = crtNode.next    # 현재 노드 건너뛰어서 삭제, 이때 prevNode는 그대로
        crtNode = crtNode.next          
      else:
        crtNode = crtNode.next          # 현재노드 하나 증가
        prevNode = prevNode.next        # 이전노드 하나 증가

    return dummyNode.next