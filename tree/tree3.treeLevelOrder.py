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

from collections import deque

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