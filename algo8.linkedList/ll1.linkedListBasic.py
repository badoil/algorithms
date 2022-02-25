# 노드들이 링크로 연결되어 있고, 전체적으로 리스트처럼 동작
# 그 노드 안에 val, ref, address 등이 있음
# 리스트는 array[4]처럼 랜덤 액세스가 가능하지만, 링크드리스트는 헤드(처음 노드)로부터 찾으려는 노드까지 연결들을 타고 가야함(횡단, traverse)
# 조회 시간복잡도 O(n), 삭제 및 삽입 시간복잡도 O(1)
# singly linked list, doubly linked list
# 링크드 리스트의 기본동작은 암기 수준으로 알고 있어야함. tree, graph 의 기본 데이터 스트럭쳐가 되기 때문

# 기본적인 링크드 리스트

class NodeList:
  def __init__(self, val):
    self.val = val
    self.next = None

node = NodeList(0)
node.next = NodeList(1)
node.next.next = NodeList(2)

def iterNode(node: NodeList):
  crtNode = node
  while crtNode is not None:
    print(crtNode.val, end=" ")
    crtNode = crtNode.next

def recurNode(node: NodeList):
  print(node.val, end=" ")
  if node.next is not None:
    recurNode(node.next)


iterNode(node)
recurNode(node)

