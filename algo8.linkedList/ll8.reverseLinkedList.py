# 206
# 문제 : 주어진 LinkedList를 뒤집어라
# 예제 : 1→3→5→7→9\
# 답 : 9→7→5→3→1

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

#Example 3:
# Input: head = []
# Output: []
 
# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000



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

def printNodes(node: ListNode):
  crtNode = node
  while crtNode:
    print(crtNode.val, end=" ")
    crtNode = crtNode.next


class ReverseList:
  def iterativeWay(self, head: ListNode) -> ListNode:
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

  def recursiveWay(self, head: ListNode) -> ListNode:
    #exit condition
    if head is None:
      return head
    elif head.next is None:
      return head    
    
    back_head = self.recursiveWay(head.next)
    head.next.next = head
    head.next = None
    
    return back_head

rvs_list = ReverseList()

head = createList([1,3,5,7,9])
rvs_head = rvs_list.iterativeWay(head)
printNodes(rvs_head)


head = createList([1,3,5,7,9])
rvs_head = rvs_list.recursiveWay(head)
printNodes(rvs_head)





################################################################################





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


class Reverse:
  def iterativeWay(self, head: ListNode) -> ListNode:
    if head is None:
      return head
    if head.next is None:
      return head

    prevNode = head
    crtNode = head.next
    head.next = None      # 역방향이기 때문에 순방향을 없애줌

    while crtNode:
      tempNextNode = crtNode.next
      crtNode.next = prevNode     # 현재 노드를 이전 노드로 연결, 역방향으로 연결
      prevNode = crtNode          # prevNode를 다음으로 처리할 노드로 이동
      crtNode = tempNextNode      # crtNode를 다음으로 처리할 노드로 이동

    return prevNode

  def recursiveWay(self, head: ListNode) -> ListNode:   # 재귀적인 방법은 노드의 끝에서부터, 노드의 방향을 역방향으로 만들며 진행
    # exit condition
    if head is None:
      return head
    if head.next is None:
      return head

    reverseHead = self.recursiveWay(head.next)    # 스택은 해당 노드의 오른쪽 끝까지 쌓이다가 head를 리턴받고(exit condition) 이 reverseHead를 계속 이전 스택으로 넘긴다
                                                  # 이때 reverseHead = head 할당 받으므로 아래 역방향 만드는 과정에서 head를 조작하면 됨, 그리고 그 reverseHead 리턴
    
    # making reverse direction
    head.next.next = head                         # 해당 헤드의 오른쪽으로 다음 다음 헤드가 해당 헤드를 가리키게 만들어서, 헤당 헤드의 바로 오른쪽에 있는 헤드의 방향이 해당 헤드로(왼쪽으로) 바뀐다
    head.next = None                              # 이때 해당 헤드의 오른쪽 방향을 없애줌

    return reverseHead                            # 리턴 받은 reverseHead를 리턴하면서 쌓였던 스택들을 pop 하다가 최종적으로 리턴