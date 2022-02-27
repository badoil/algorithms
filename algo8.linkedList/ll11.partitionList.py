# 86

# 문제 : 주어진 List를 x보다 작은수를 먼저, x보다 큰수를 나중에 나오도록 partition하여라. 이때 순서가 list안 node의 순서가 바뀌면 안된다
# input : 1→3→7→5→3→6→3, x=5 \
# 답 :  1→3→3→7→5→6

from typing import List

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

def createNodeList(nums: List[int]) -> ListNode:
  if len(nums) == 0:
    raise RuntimeError('empty')

  head = ListNode(nums[0])
  crtNode = head
  for idx in range(1, len(nums)):
    print(crtNode.val, end=" ")
    node = ListNode(nums[idx])
    crtNode.next = node
    crtNode = node

  return head

def printNodes(node:ListNode):
  crnt_node = node
  while crnt_node is not None:
    print(crnt_node.val, end=' ')
    crnt_node = crnt_node.next
  print()

class Partitioner:
  def partition(self, head: ListNode, x: int) -> ListNode:
    dummy_a = ListNode(-1)
    dummy_b = ListNode(-1)
    
    node_a = dummy_a
    node_b = dummy_b
    
    crnt_node = head
    while crnt_node:
      val = crnt_node.val
      if x <= val:
        node_b.next = crnt_node
        node_b = node_b.next
        crnt_node = crnt_node.next
      else:
        node_a.next = crnt_node
        node_a = node_a.next
        crnt_node = crnt_node.next
        
    node_b.next = None
    node_a.next = dummy_b.next
    
    return dummy_a.next

partitioner = Partitioner()

head = createNodeList([1,3,7,5,3,6])
partition_head = partitioner.partition(head,5)
printNodes(partition_head)


#########################################################################################



class Partition:
  def partitioning(self, head: ListNode, val: int) -> ListNode:   # 두 노드를 val을 기준으로 각각 만들다가, 나중에 연결시킨다
    dummyA = ListNode(-1)
    dummyB = ListNode(-1)

    crtNode = head
    crtNodeA = dummyA
    crtNodeB = dummyB
    while crtNode:
      crtVal = crtNode.val
      if crtVal >= val:                 # val보다 크면 crtNodeB로 연결
        crtNodeB.next = crtNode
        crtNodeB = crtNodeB.next
        crtNode = crtNode.next

      else:                             # val보다 작으면 crtNodeA로 연결
        crtNodeA.next = crtNode
        crtNodeA = crtNodeA.next
        crtNode = crtNode.next

    crtNodeB.next = None              # 뒤에 있는 crtNodeB의 마지막 노드의 next는 None
    crtNodeA.next = dummyB.next       # 앞에 있는 crtNodeA의 마지막 노드의 next는 crtNodeB의 첫 노드(dummyB.next)
    return dummyA.next