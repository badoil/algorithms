from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node5.left = node6
node5.right = node7

def printNode(node: TreeNode):
  q = deque()
  q.append(node)
  while q:
    count = len(q)
    for _ in range(0, count):
      node = q.popleft()
      print(node.val, end=' ')
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)

    print('')


class LCA:
  def find(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if node is None:
      return None
    
    self._p = p
    self._q = q
    
    self._found = None
    self._recurFind(node)
    
    return self._found
    
  def _recurFind(self, node):
    found = 0        #default False
    left_found = 0   #default False
    right_found = 0  #default False
    
    if node == self._p:
      found = 1    
    if node == self._q:
      found = 1      
    
    if node.left:
      left_found = self._recurFind(node.left)    
    if node.right:
      right_found = self._recurFind(node.right)
      
    found_count = found+left_found+right_found
    if found_count == 2:  #when two of three cases are True
      self._found = node
    
    if 0<found_count:
      return 1
    else:
      return 0
  
lca = LCA()

lca_node = lca.find(root,node4,node6)
print(lca_node.val)

##############################

class LCAA:
  def find(self, root: TreeNode, p:TreeNode, q:TreeNode) -> TreeNode:
    if root is None:
      return None

    self._p = p
    self._q = q

    self._found = None
    self._findNode(root, p, q)

    return self._found

  def _findNode(self, node: TreeNode):
    found = 0
    leftFound = 0
    rightFound = 0

    if node == self._p:
      found = 1

    if node == self._q:
      found = 1

    if node.left:
      leftFound = self._findNode(node.left)
    if node.right:
      rightFound = self._findNode(node.right) 

    check = found + leftFound + rightFound
    if check == 2:
      self._found = node

    if check > 0:
      return 1
    else:
      return 0

lcaa = LCAA()

lcaa_node = lcaa.find(root,node4,node6)
print(lca_node.val)