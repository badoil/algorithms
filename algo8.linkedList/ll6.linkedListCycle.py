# 876
# 문제 : 주어진 LinkedList에 cycle이 있는지 확인하여라
# 풀이1(hashWay): 해쉬셋을 이용해서 현재 노드가 거쳐온 노드인지 판단, 시간복작도 O(n) 공간복잡도 O(n)
# 풀이2(fastSlowWay):  공간복잡도 O(1)으로 풀어라. fastSlowWay 적용하면 싸이클이 존재한다면 빠른노드와 느린노드는 결국 만나게 됨

from typing import List

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

def createList(in_list:List[int]) -> ListNode:
  if len(in_list) == 0:
    raise RuntimeError("in_list must have data")        
  head_node = ListNode(in_list[0])
  last_node = head_node
  for idx in range(1,len(in_list)):
    node = ListNode(in_list[idx])
    last_node.next = node
    last_node = node
  return head_node

def makeLoop(head:ListNode, node_idx:int):
  end_node = head
  while end_node.next:
    end_node = end_node.next

  idx = 0
  crnt_node = head
  for idx in range(1,node_idx):
    crnt_node = crnt_node.next
  end_node.next = crnt_node

list_in = createList([1,3,5,7,9])
makeLoop(list_in,2)


class HasLoop:
  def hashWay(self, head: ListNode) -> bool:
    if head is None:
      return False

    node_set = set()
    crnt_node = head
    while crnt_node:
      if crnt_node in node_set:
        return True
      node_set.add(crnt_node)
      crnt_node = crnt_node.next
        
    return False

  def fastSlow(self, head: ListNode)-> bool:
    if head is None:
      return False
    
    slow_node = head
    fast_node = head
    while fast_node:
      if fast_node.next:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
      else:
        break
        
      if fast_node == slow_node:
        return True
      
    return False


hasLoop = HasLoop()
hasLoop.hashWay(list_in)
hasLoop.fastSlow(list_in)


###########################################################



def makeNodeList(nums: List[int]) -> ListNode:
  if len(nums) == 0:
    raise RuntimeError("empty")

  headNode = ListNode(nums[0])
  crtNode = headNode
  for idx in range(1, len(nums)):
    nextNode = ListNode(nums[idx])
    crtNode.next = nextNode
    crtNode = nextNode

  return headNode

def printNode(node: ListNode):
  crtNode = node
  while crtNode:
    print(crtNode.val, end=" ")
    crtNode - crtNode.next


def makeCycle(node: ListNode, nodeIdx: int):
  endNode = node
  while endNode:
    endNode = endNode.next

  crtNode = node
  for _ in range(1, nodeIdx):
    crtNode = crtNode.next

  endNode.next = crtNode


class Cycle:
  def hashWay(self, node: ListNode) -> bool:
    if node is None:
      return False

    hashSet = set()
    crtNode = node
    while crtNode:
      if crtNode in hashSet:
        return True
      hashSet.add(crtNode)
      crtNode = crtNode.next

    return False

  def fastSlowWay(self, node: ListNode) -> bool:
    if node is None:
      return False

    fast = node
    slow = node
    while fast:
      if fast.next:
        fast = fast.next.next
        slow = slow.next
      else:
        break

      if fast.val == slow.val:
        return True

    return False