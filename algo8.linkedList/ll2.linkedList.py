# Title : S linked list

# 노드들을 묶어서 전체적인 클래스를 만든다
# 보통 라이브러리가 제공되지만 여기서 직접 구현해봄
# 클래스로 oop 개념으로 만들어보자
# addAtHead, addAtBack, addAfter, find, deleteAfter 라는 인터페이스(함수) 만들거임

# 코테에서는 링크드 리스트의 오브젝트가 아니라 이미 말들어져있는 링크드 리스트의 헤드 정보만 알려줌


class NodeList:
  def __init__(self, val):
    self.val = val
    self.next = None

def printNodes(node:ListNode):
  crnt_node = node
  while crnt_node is not None:
    print(crnt_node.val, end=' ')
    crnt_node = crnt_node.next

class SLinkedList:
  def __init__(self):
    self.head = None

  def addAtHead(self, val): #O(1)
    node = ListNode(val)
    node.next = self.head
    self.head = node

  #but when the list
  def addBack(self, val): #O(n)
    node = ListNode(val)
    crnt_node = self.head
    while crnt_node.next:
      crnt_node = crnt_node.next
    crnt_node.next = node

  def findNode(self, val): #O(n)
    crnt_node = self.head
    while crnt_node is not None:
      if crnt_node.val == val:
        return crnt_node
      crnt_node = crnt_node.next
    raise RuntimeError('Node not found')

  def addAfter(self, node, val): #O(1)
    new_node = ListNode(val)
    new_node.next = node.next
    node.next = new_node

  def deleteAfter(self, prev_node): #O(1)
    if prev_node.next is not None:
      prev_node.next = prev_node.next.next


slist = SLinkedList()
slist.addAtHead(1)
slist.addAtHead(2)
slist.addBack(3)

node1 = slist.findNode(1)
slist.addAfter(node1,4)
slist.deleteAfter(node1)
printNodes(slist.head)


###########################################3


def iterNode(node: NodeList):
  crtNode = node
  while crtNode is not None:
    print(crtNode.val, end=" ")
    crtNode = crtNode.next

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def addAtHead(self, val):
    node = NodeList(val)
    node.next = self.head
    self.head = node

  def addAtBack(self, val):
    node = NodeList(val)
    crtNode = self.head
    while crtNode is not None:
      crtNode = crtNode.next
    crtNode.next = node

  def findNode(self, val):
    crtNode = self.head
    while crtNode is not None:
      if crtNode.val == val:
        return crtNode
      crtNode = crtNode.next
    raise RuntimeError('not found')

  def addAfter(self, node, val):
    newNode = NodeList(val)
    newNode.next = node.next
    node.next = newNode

  def deleteAfter(self, prevNode):        # 지우려는 노드를 찾고 지우려면 O(n) 걸리기에, 바로 그 전 노드를 안다고 가정하면 O(1) 로 지울 수 있음
    if prevNode.next is not None:         # 매니지드 언어에서는 지우려고 하는 prevNode의 다음 노드가 자동으로 삭제도지만 언매니지드에서는 직접 지워줘야함 
      prevNode.next = prevNode.next.next  # 더블리 링크드 리스트였다면 prevNode 가 아니라 지우려는 노드 node를 넣어도 됨