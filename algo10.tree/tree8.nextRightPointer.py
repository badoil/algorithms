# 117


from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.next = None

def treeLevelPrint(node):
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


root = TreeNode(1)
node3 = TreeNode(3)
node5 = TreeNode(5)
node7 = TreeNode(7)
node9 = TreeNode(9)
node2 = TreeNode(2)

root.left = node3
root.right = node5
node3.left = node7
node3.right = node9
node5.right = node2

treeLevelPrint(root)


class MakeNext:
  def _connect(self, prev_node, next_node):
    if prev_node:
      prev_node.next = next_node     
  
  def connect(self, root):
    if root is None:
      return None    
    level_node = root
    
    while level_node:
      crnt_node = level_node
      next_level = None
      prev_child = None
      
      while crnt_node:        
        if crnt_node.left:
          self._connect(prev_child,crnt_node.left)          
          prev_child = crnt_node.left
          if next_level is None:
            next_level = crnt_node.left

        if crnt_node.right:
          self._connect(prev_child,crnt_node.right)
          prev_child = crnt_node.right
          if next_level is None:
            next_level = crnt_node.right
        crnt_node = crnt_node.next      
      level_node = next_level    
    return root

makeNext = MakeNext()
root = makeNext.connect(root)

##############################################

class MakeNextt:
  def _connect(self, prevNode: TreeNode, nextNode: TreeNode):
    if prevNode:
      prevNode.next = nextNode

  def connect(self, root: TreeNode):
    if root is None:
      return None

    rootNode = root
    while rootNode:
      crtNode = rootNode
      prevNode = None
      nextLevelNode = None

      while crtNode:
        if crtNode.left:
          self._connect(prevNode, crtNode.left)
          prevNode = crtNode.left
          if nextLevelNode is None:
            nextLevelNode = crtNode.left

        if crtNode.right:
          self._connect(prevNode, crtNode.right)
          prevNode = crtNode.right
          if nextLevelNode is None:
            nextLevelNode = crtNode.right
        crtNode = crtNode.next
      rootNNode = nextLevelNode 
    return root