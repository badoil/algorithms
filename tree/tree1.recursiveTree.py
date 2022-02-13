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

  print(node.val, end=' ')
  preorder(node.left)
  preorder(node.right)

preorder(node1)

#LNR
def inorder(node: TreeNode):
  if node is None:
    return

  inorder(node.left)
  print(node.val, end=' ')
  inorder(node.right)

inorder(node1)

#LRN
def postorder(node: TreeNode):
  if node is None:
    return 

  postorder(node.left)
  postorder(node.right)
  print(node.val, end=' ')

postorder(node1)