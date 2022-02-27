# 2(역방향), 445(정방향)
# 문제 : 주어진 LinkedLists의 역방향 합과 정방향 합을 구하여라
# list1 : 7→5→3  정 753, 역 357 
# list2 : 4→8→2  정 482, 역 284
# 역방향 답 : 1→4→6
# 정방향 답 :  1→2→3→5

# 링크드 리스트의 덧셈은 역방향이 편하다. 헤드 노드가 캐리를 가지고 다음 수로 넘어가기 때문임
# 따라서 순방향 덧셈은 역방향으로 리스트들을 바꿔주고 이를 역방향 덧셈을 해준 후, 다시 이를 순방향으로 바꿔서 리턴

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


class ListAdder:
  def addReverse(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy_node = ListNode(-1)
    crnt_node = dummy_node
    node_a = l1
    node_b = l2
    carry = 0
    
    while node_a or node_b:
      num_a = node_a.val if node_a else 0
      num_b = node_b.val if node_b else 0
      sum_ab = num_a + num_b + carry
      carry = int(sum_ab / 10)
      val = int(sum_ab % 10)
      
      new_node = ListNode(val)
      crnt_node.next = new_node
      crnt_node = crnt_node.next
      node_a = node_a.next if node_a else None
      node_b = node_b.next if node_b else None   
    
    if 1 == carry:
      new_node = ListNode(carry)
      crnt_node.next = new_node

    return dummy_node.next

  def addForward(self, l1: ListNode, l2: ListNode) -> ListNode:
    reverse_head1 = self.__reverseList(l1)
    reverse_head2 = self.__reverseList(l2)

    reverse_sum = self.addReverse(reverse_head1,reverse_head2)
    forward_sum = self.__reverseList(reverse_sum)
    return forward_sum

  def __reverseList(self, head: ListNode) -> ListNode:
    if head is None:
      return head
    elif head.next is None:
      return head    
    
    crnt_node = head.next
    prev_node = head
    head.next = None
    
    while crnt_node:
      tmp_next_node = crnt_node.next
      crnt_node.next = prev_node
      prev_node = crnt_node
      crnt_node = tmp_next_node
      
    return prev_node

adder = ListAdder()

list1 = createList([7,5,3])
list2 = createList([4,8,2])
reverseAdd = adder.addReverse(list1,list2)
printNodes(reverseAdd)

list1 = createList([7,5,3])
list2 = createList([4,8,2])
reverseAdd = adder.addForward(list1,list2)
printNodes(reverseAdd)



###################################################################################



class Add:
  def reverseAdd(self, nodeA: ListNode, nodeB: ListNode) -> ListNode:
    dummyNode = ListNode(-1)
    crtNode = dummyNode

    carry = 0
    while nodeA or nodeB:
      valA = nodeA.val if nodeA else 0
      valB = nodeB.val if nodeB else 0

      sum = valA + valB + carry
      carry = int(sum/10)
      newVal = int(sum%10)        # 나머지를 구함, 몫0 이면 나머지는 sum

      newNode = ListNode(newVal)
      crtNode.next = newNode
      crtNode = newNode

      nodeA = nodeA.next if nodeA else None
      nodeB = nodeB.next if nodeB else None

    if carry == 1:
      node = ListNode(1)
      crtNode.next = node

    return dummyNode.next


  def add(self, nodeA: ListNode, nodeB: ListNode) -> ListNode:
    revNodeA = self.makeReverseLinkedList(nodeA)                # 링크드 리스트의 덧셈은 역방향이 편하다. 헤드 노드가 캐리를 가지고 다음 수로 넘어가기 때문임
    revNodeB = self.makeReverseLinkedList(nodeB)                

    revAdd = self.reverseAdd(revNodeA, revNodeB)                # 따라서 순방향 덧셈은 역방향으로 리스트들을 바꿔주고 이를 역방향 덧셈을 해준 후, 다시 이를 순방향으로 바꿔서 리턴
    result = self.makeReverseLinkedList(revAdd)
    return result


  def makeReverseLinkedList(self, head: ListNode) -> ListNode:
    if head is None:
      return head
    elif head.next is None:
      return head

    prevNode = head
    crtNode = head.next
    head.next = None       # 남아있는 헤드의 순방향 넥스트 제거
    while crtNode:
      tempNextNode = crtNode.next
      crtNode.next = prevNode
      prevNode = crtNode
      crtNode = tempNextNode

    return prevNode