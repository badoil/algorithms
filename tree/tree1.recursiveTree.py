# full binary tree: 자식 노드가 없거나 자식 노드 2개가 다 있는 노드만 있는 트리
# complete binary tree: 왼쪽 위에서부터 가득 차 있는 바이너리 트리, 위에서부터 왼쪽만 정렬되어 있으면 됨
# perfect binary tree: 자식 노드를 모두 가지고 있고, leaf가 모두 같은 레벨에 있는 트리

# tree traverse(트리 이동) 하는 방법: preorder, inorder, postorder
# preorder: NLR(부모노드 -> 왼쪽 자식노드 -> 오른쪽 자식노드) N(부모노드)가 맨 앞에 온다
# inorder: LNR(왼쪽 자식노드 -> 부모노드 -> 오른쪽 자식노드) N(부모노드)가 가운데에 온다
# postorder: LRN(왼쪽 자식노드 -> 오른쪽 자식노드 -> 부모노드) N(부모노드)가 맨 뒤에 온다


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