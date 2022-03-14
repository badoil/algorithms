# 876
# 문제 : 주어진 LinkedList의 중간 node를 찾아서 return하여라 \
# 예제1 : 1→3→5→7→9 \
# output : 5→7→9 \
# 예제2 : 1→2→3→4 \
# output : 3→4


# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100


# 풀이법1(countWay): 링크드 리스트의 총 카운트를 세서 중간 값을 구하고, 그 값까지 next반복하므로 총 2번의 반복문 필요
# 풀이법2(arrayWay): 링크드 리스트를 배열에 넣고, 중간 인덱스로 구하고자 하는 노드 찾기, 배열에 링크드 리스트 넣을때 1번의 반목문 필요, 그러나 O(n)공간복잡도가 배열 때문에 필요
# 풀이법3(fastSlowWay): fast & slow pointer 방법,  O(1)공간복잡도, 


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


class MiddleNode:
  def indexWay(self, head:ListNode) -> ListNode:
    total_count = 0
    crnt_node = head
    while crnt_node:
      total_count += 1
      crnt_node = crnt_node.next
    
    half_count = int(total_count/2)
    
    crnt_node = head
    for idx in range (0,half_count):
      crnt_node = crnt_node.next
      
    return crnt_node

  def arrayWay(self, head:ListNode) -> ListNode:
    node_array = []
    crnt_node = head
    while crnt_node:
      node_array.append(crnt_node)
      crnt_node = crnt_node.next       
    half_count = len(node_array)//2
    return node_array[half_count]


  def fastSlow(self, head:ListNode) -> ListNode:
    slow_node = head
    fast_node = head
    
    while fast_node:
      if fast_node.next:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
      else:
        break
        
    return slow_node

#index way
list_in = createList([1,3,5,7,9])
middle_node = MiddleNode()
middle_node = middle_node.indexWay(list_in)
printNodes(middle_node)

#array way
list_in = createList([1,3,5,7,9])
middle_node = MiddleNode()
middle_node = middle_node.arrayWay(list_in)
printNodes(middle_node)




###################################################################################
# 풀이법1(countWay): 링크드 리스트의 총 카운트를 세서 중간 값을 구하고, 그 값까지 next반복하므로 총 2번의 반복문 필요
# 풀이법2(arrayWay): 링크드 리스트를 배열에 넣고, 중간 인덱스로 구하고자 하는 노드 찾기, 배열에 링크드 리스트 넣을때 1번의 반목문 필요, 그러나 O(n)공간복잡도가 배열 때문에 필요
# 풀이법3(fastSlowWay): fast & slow pointer 방법,  O(1)공간복잡도, 



class Middle:
  def countWay(self, node: ListNode) -> ListNode:
    count = 0
    crtNode = node

    while crtNode is not None:
      count += 1
      crtNode = crtNode.next

    half = int(count/2)
    resultNode = node
    for _ in range(half):             # 해당 노드의 바로 전까지 포문을 돈다. 
      resultNode = resultNode.next    # 그래야 resultNode.next 가 해당 노드가 됨

    return resultNode


  def arrayWay(self, node: ListNode) -> ListNode:
    nodeList = []
    crtNode = node
    while crtNode is not None:
      nodeList.append(crtNode)
      crtNode = crtNode.next

    count = len(nodeList)
    half = count//2
    
    return nodeList[half]


  def fastSlowWay(self, node: ListNode) -> ListNode:    # fastNode가 2칸씩, slowNode가 1칸씩 가기에, fastNode가 끝날때 slowNode의 위치가 노드의 중간임
    fastNode = node
    slowNode = node

    while fastNode is not None:
      if fastNode.next is not None:
        fastNode = fastNode.next.next
        slowNode = slowNode.next
      else:
        break

    return slowNode