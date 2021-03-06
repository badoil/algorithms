# 141
# 문제 : 주어진 LinkedList에 cycle이 있는지 확인하여라

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 
# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.


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





###############################################################################
# 풀이1(hashWay): 해쉬셋을 이용해서 현재 노드가 거쳐온 노드인지 판단, 시간복작도 O(n) 공간복잡도 O(n)
# 풀이2(fastSlowWay):  공간복잡도 O(1)으로 풀어라. fastSlowWay 적용하면 싸이클이 존재한다면 빠른노드와 느린노드는 결국 만나게 됨




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

      if fast.val == slow.val:    # 싸이클이 존재한다면 빠른노드와 느린노드는 결국 만나게 됨
        return True

    return False