# iterative tree traversal은 그래프 자료구조 BFS DFS의 특수 케이스
# 특히 postorder가 BFS DFS와 연관

# 얘는 좀 외울 필요가 있겠음

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


# NLR
def preorder(node: TreeNode):
  if node is None:
    return

  stack = []
  stack.append(node)

  while len(stack) > 0:
    popStack = stack.pop()
    print(popStack.val, end=' ')
    if popStack.right:
      stack.append(popStack.right)
    
    if popStack.left:
      stack.append(popStack.left)

preorder(node1)


#LNR
def inorder(node:TreeNode):
  if node is None:
    return

  stack=[]
  crtNode = node
  while True:
    if crtNode is not None:
      stack.append(crtNode)
      crtNode = crtNode.left

    elif len(stack) > 0:
      popStack = stack.pop()
      print(popStack.val, end=' ')
      crtNode = popStack.right
    else:
      break

inorder(node1)


#LRN
def iterativePostorder(node):
  stack = []
  last_visit_node = None
  crnt_node = node
  while True:
    if crnt_node is not None:
      stack.append(crnt_node)
      crnt_node = crnt_node.left
    
    elif 0<len(stack):
      peek_node = stack[-1]
      if peek_node.right and last_visit_node != peek_node.right:
        crnt_node = peek_node.right
      else:
        print(peek_node.val, end=' ')
        last_visit_node = stack.pop()
        
    else:
      break

iterativePostorder(node1)