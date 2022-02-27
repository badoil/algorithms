# 138
# 문제 : random node가 포함된 linked list를 deep copy 하여라.

# 이번에 노드에는 val, next 뿐만 아니라 randomPointer가 들어감
# 이때 문제는 한 노드의 랜덤 노드는 원본 노드에서 알수 있어도, 복사된 노드에서 그 랜덤노드로 갈 방법이 없다는 것

# 풀이법1(hashWay): 시간복잡도 O(n), 해쉬맵을 쓰기에 공간복잡도 O(n) 
# 풀이법2(nodeMatch): 시간복잡도 O(n), 공간복잡도 O(1) 이 방법은 해쉬맵을 쓰지 않고 노드들 자체만 사용해서 풀이

from typing import List
import random


class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.random = None

def makeRandomNode(head: ListNode) -> ListNode:
  crtNode = head
  nodeArray = []
  while crtNode:
    nodeArray.append(crtNode)
    crtNode = crtNode.next

  crtNode = head
  while crtNode:
    randNum = random.randint(0, len(nodeArray)-1)
    crtNode.random = nodeArray[randNum]
    crtNode = crtNode.next

  return head


class Copy:
  def hashWay(self, head: ListNode) -> ListNode:
    if head is None:
      return None

    hashMap = {}
    dummy = ListNode(-1)
    crtNodeR = head
    crtNodeW = dummy
    while crtNodeR:
      rVal = crtNodeR.val
      tempNode = ListNode(rVal)
      hashMap[crtNodeR] = tempNode

      crtNodeW.next = tempNode
      crtNodeW = tempNode
      crtNodeR = crtNodeR.next

    crtNodeR = head
    while crtNodeR:
      startNode = hashMap[crtNodeR]
      randomNode = crtNodeR.random
      endNode = None
      if randomNode is not None:
        endNode = hashMap[randomNode]        

      startNode.random = endNode
      crtNodeR = crtNodeR.next

    return dummy.next


  def nodeMatchWay(self, head: ListNode) -> ListNode:
    if head is None:
      return None

    crtNode = head
    while crtNode:                  # 두 노드를 서로 지그재그로 next를 이용해서 연결시킴
      val = crtNode.val
      tempNode = ListNode(val)

      tempNode.next = crtNode.next
      crtNode.next = tempNode
      crtNode = tempNode


    crtNode = head
    while crtNode:                   # 지그재그 형태를 가지면, 원본 노드의 next는 동일한 값을 가지는 복사본 노드를 가리키게 됨
      tempNode = crtNode.next
      randomNode = crtNode.random
      toNode = None
      if randomNode is not None:
        toNode = crtNode.random.next   # 원본 노드의 random의 next가 복사본 노드의 random이 가리켜야할 노드
      tempNode.random = toNode

      crtNode = crtNode.next.next

    crtNode = head
    dummy = ListNode(-1)              # 새롭게 카피한 노드를 리턴하기 위해서 더미 노드 필요함
    dummy.next = crtNode.next
    while crtNode and crtNode.next:   # crtNode.next 도 조건으로 들어가는 이유는 마지막 노드는 처리할 필요가 없기 때문임
      tempNode = crtNode.next

      crtNode.next = crtNode.next.next
      crtNode = tempNode
    
    return dummy.next