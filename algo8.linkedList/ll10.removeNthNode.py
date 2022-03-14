# 19
# 문제 : 뒤에서 n번째 node를 삭제하여라
# input : 1→3→5→7→9, n=2 \
# 답 :  1→3→5→9

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
 
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# 이건 직접 풀어보자

# two pass, counter 
# array
# two nodes, one pass 



from typing import List

class ListNode:
  def __init__(self, x):
    self.val = x
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


class RemoveNthBack:
  def countBase(self, head: ListNode, n: int) -> ListNode:
    if n==0:
      return head
    
    list_count = 0
    crnt_node = head
    while crnt_node:
      crnt_node = crnt_node.next 
      list_count += 1
    
    count_togo = list_count - n
    dummy_node = ListNode(0)
    dummy_node.next = head
    crnt_node = dummy_node
    for _ in range(0, count_togo):
      crnt_node = crnt_node.next
    
    crnt_node.next = crnt_node.next.next
    return dummy_node.next

  def arrayApproach(self, head: ListNode, n: int) -> ListNode:
    if n==0:
      return head
    
    dummy_node = ListNode(-1)
    dummy_node.next = head    
    crnt_node = dummy_node
    node_list = []
    while crnt_node:
      node_list.append(crnt_node)
      crnt_node = crnt_node.next
      
    delete_idx = len(node_list)-n
    prev_idx = delete_idx -1
    prev_node = node_list[prev_idx]
    prev_node.next = prev_node.next.next
    
    return dummy_node.next

  def twoPointers(self, head: ListNode, n: int) -> ListNode:
    if n==0:
      return head
    
    dummy_node = ListNode(-1)
    dummy_node.next = head    
    first_node = dummy_node

    for _ in range(0,n+1):
      first_node = first_node.next
      
    second_node = dummy_node
    while first_node:
      first_node = first_node.next
      second_node = second_node.next
    
    second_node.next = second_node.next.next    
    return dummy_node.next
        
remover = RemoveNthBack()

in_list = createList([1,3,5,7,9])
out_list = remover.countBase(in_list,2)
printNodes(out_list)




######################################################################################

