# 160
# 문제 : 주어진 LinkedList의 교차점을 return하여라

# 풀이1(hashWay): 해쉬셋을 이용해서 현재 노드가 거쳐온 노드인지 판단, 시간복작도 O(n) 공간복잡도 O(n)
# 풀이2(twoNodesWay):  공간복잡도 O(1)으로 풀어라. 두 노드의 현재노드들을 동시에 nodeA nodeB를 거치게 한 후 각각 교차해서 다시 처음부터 시작하면 교차점에서 만나게됨.

from typing import List

class ListNode:
  def __init(self, val):
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

def getIdxNode(head:ListNode, idx:int):
  nth_node = head
  for idx in range (0,idx):
    nth_node = nth_node.next
  return nth_node

list_a = createList([1,3,5,7,9])
list_b = ListNode(2)
intersection = getIdxNode(list_a,3)
list_b.next = intersection

#list a 1-3-5 \
#              7 - 9
#list b     2 /
#intersection is seven


class IntersectionFinder:
  def twoNodesWay(self, headA: ListNode, headB: ListNode) -> ListNode:
    node_a = headA
    node_b = headB    
    while node_a != node_b:
      if node_a:
        node_a = node_a.next
      else:
        node_a = headB
        
      if node_b:
        node_b = node_b.next
      else:
        node_b = headA
        
    return node_a

  def hashWay(self, headA:ListNode, headB:ListNode) -> ListNode:
    node_set = set()
    
    crnt_node = headA
    while crnt_node:
      node_set.add(crnt_node)
      crnt_node = crnt_node.next
      
    crnt_node = headB
    while crnt_node:
      if crnt_node in node_set:
        return crnt_node
      crnt_node = crnt_node.next
      
    return None
      
finder = IntersectionFinder()  

print(finder.twoNodesWay(list_a,list_b).val)
print(finder.hashWay(list_a,list_b).val)


##########################################################################


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


def intersectionNode(node: ListNode, nodeIdx: int) -> ListNode:
  crtNode = node
  for _ in range(nodeIdx):
    crtNode = crtNode.next
  return crtNode


class Intersection:
  def twoNodesWay(self, nodeA: ListNode, nodeB: ListNode) -> ListNode:
    crtNodeA = nodeA
    crtNodeB = nodeB

    while crtNodeA != crtNodeB:
      if crtNodeA:                
        crtNodeA = crtNodeA.next
      else:                       # crtNodeA 끝났으면 nodeB로 교체
        crtNodeA = nodeB

      if crtNodeB:
        crtNodeB = crtNodeB.next
      else:                       # crtNodeB 끝났으면 nodeA로 교체
        crtNodeB = nodeA

    return crtNodeA               # 이렇게 교체해주면 두 노드의 교차저믕로부터의 거리차가 없어지고 동식에 교차점에서 만남


  def hashWay(self, nodeA: ListNode, nodeB: ListNode) -> ListNode:
    hashSet = set()
    crtNodeA = nodeA
    while crtNodeA:
      hashSet.add(crtNodeA)
      crtNodeA = crtNodeA.next

    crtNodeB = nodeB
    while crtNodeB:
      if crtNodeB in hashSet:
        return crtNodeB

      crtNodeB = crtNodeB.next

    return None