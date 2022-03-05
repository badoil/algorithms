# 각 레벨의 왼쪽에서 오른쪽으로 출력한 뒤, 다음 레벨로 이동해서 다시 왼쪽에서 오른쪽으로 출력
# 이는 그래프의 bfs로 볼 수 있음
# 큐를 이용해서 풀 수 있는 것


from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


def treeLevelPrint(node):
  if node is None:
    return
  q = deque()
  q.append(node)
  while 0<len(q):
    crnt_node = q.popleft()
    print(crnt_node.val, end = ' ')
    if crnt_node.left:
      q.append(crnt_node.left)
    if crnt_node.right:
      q.append(crnt_node.right)
    

treeLevelPrint(node1)

def treeLevelPrint2(node):
  if node is None:
    return
  q = deque()
  q.append(node)
  while 0<len(q):
    level_count = len(q)
    for _ in range(level_count):
      crnt_node = q.popleft()
      print(crnt_node.val, end = ' ')
      if crnt_node.left:
        q.append(crnt_node.left)
      if crnt_node.right:
        q.append(crnt_node.right)
    print('')
treeLevelPrint2(node1)


##########################################################


def printNodes(head: TreeNode):
  if node is None:
    return

  q = deque()
  q.append(head)
  while q:
    count = len(q)
    for _ in range(count):
      node = q.popleft()
      print(node.val, end=" ")
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    print('')



def treeLevelOrder(node: TreeNode):
  if node is None: 
    return

  q = deque
  q.append(node)
  while len(q) > 0:
    crtnode = q.popleft()
    print(crtnode.val, end=' ')
    
    if crtnode.left:
      q.append(crtnode.left)
    
    if crtnode.right:
      q.append(crtnode.right)

treeLevelOrder(node1)