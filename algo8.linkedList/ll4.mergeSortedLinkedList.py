# 문제 : 주어진 두개의 정렬된 LinkedList를 정렬이 된 상태로 합쳐라 \
# L1 :    1→3→5→7 \
# L2 :    1→2→3→4
# L1+L2 : 1→1→2→3→3→4→5→7

# len(linkedList1) = m, len(linkedList2) = n 일때, 시간복잡도 O(m+n)
# 처음 더미노드 만들면서 O(1)의 공간복잡도
# 기본적으로 오름차순으로 정렬되어 있기 때문에 가능한 알고리즘


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

def printNodes(node:ListNode):
  crnt_node = node
  while crnt_node is not None:
    print(crnt_node.val, end=' ')
    crnt_node = crnt_node.next
  print()


class MergeTwoLists:
  def iterativeWay(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy_node = ListNode(0)
    crnt_node = dummy_node
    
    node1 = l1
    node2 = l2
    
    while node1 and node2:
      val1 = node1.val
      val2 = node2.val      
      if val1<=val2:
        crnt_node.next = node1
        node1 = node1.next
        crnt_node = crnt_node.next
      else:
        crnt_node.next = node2
        node2 = node2.next
        crnt_node = crnt_node.next
    
    if node1:
      crnt_node.next = node1
    else:
      crnt_node.next = node2
        
    return dummy_node.next

  def recursiveWay(self, l1: ListNode, l2: ListNode) -> ListNode:
    #exit conditions
    if l1 is None:
      return l2
    elif l2 is None:
      return l1    
    
    if l1.val <= l2.val:
      l1.next = self.recursiveWay(l1.next,l2)
      return l1
    else:
      l2.next = self.recursiveWay(l1,l2.next)
      return l2    

#itearative Way
list1 = createList([1,3,5,7])
list2 = createList([1,2,3,4])

merger = MergeTwoLists()
merged_head = merger.iterativeWay(list1,list2)
printNodes(merged_head)


#recursiveWay Way
list1 = createList([1,3,5,7])
list2 = createList([1,2,3,4])

merger = MergeTwoLists()
merged_head = merger.recursiveWay(list1,list2)
printNodes(merged_head)

    

#######################################################################

def createNodeList(nums: List[int]):
  if len(nums) == 0:
    raise RuntimeError("empty")

  headNode = ListNode(nums[0])
  lastNode = headNode

  for idx in range(1, len(nums)):
    node = ListNode(nums[idx])
    lastNode.next = node
    lastNode = node

  return headNode

def printNodes(node: ListNode):
  crtNode = node
  while crtNode is not None:
    print(crtNode.val, end=" ")
    crtNode = crtNode.next

  

class Merge:
  def iterativeMerge(self, node1: ListNode, node2: ListNode) -> ListNode:     
    dummyNode = ListNode(0)         # 새로운 노드를 형성하기 위한 더미노드                     
    crtNode = dummyNode 

    while crtNode is not None:      # crtNode가 두 노드의 값 중 더 작은 값을 가지는 노드를 따라가면서 새로운 노드를 형성
      if node1.val <= node2.val:
        crtNode.next = node1
        node1 = node1.next
      else:
        crtNode.next = node2
        node2 = node2.next

    if node1 is not None:           # 따라서 crtNode 는 두 노드 중 한 곳에서 끝까지 가게됨. 그때 다른 노드가 남게 되는데 이를 연결해줌
      crtNode.next = node1

    if node2 is not None:
      crtNode.next = node2

    return dummyNode.next


  def recurMerge(self, node1: ListNode, node2: ListNode):
    if node1 is None:     # 남은 노드가 node2 라는 의미이기 때문에 node2를 리턴해줌
      return node2

    if node2 is None:
      return node1

    if node1.val <= node2.val:
      node1.next = self.recurMerge(node1.next, node2)       # 스택을 생각할것!
      return node1
    else:
      node2.next = self.recurMerge(node1, node2.next)
      return node2