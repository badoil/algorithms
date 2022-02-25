# 203 
# remove linked list elements
# 여러 엘리먼트들 삭제하기

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
    node = NodeList[idx]
    lastNode.next = node
    lastNode = node

  return headNode

def printNodes(node: NodeList):
  crtNode = node
  while crtNode is not None:
    print(crtNode.val, end=" ")
    crtNode= crtNode.next


class RemoveElements:
  def __init__(self, val):        # 지우고 싶은 노드의 밸류가 객체를 생성할 때 생성자로 들어옴
    self._val = val

  def _recurRemove(self, node: NodeList) -> NodeList:   # 재귀적인 방법은 더미노드가 필요없음
    if not node:
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
        prevNode.next = crtNode.next    # 현재 노드 건너뛰어서 삭제
        crtNode = crtNode.next          
      else:
        crtNode = crtNode.next          # 현재노드 하나 증가
        prevNode = prevNode.next        # 이전노드 하나 증가

    return dummyNode.next