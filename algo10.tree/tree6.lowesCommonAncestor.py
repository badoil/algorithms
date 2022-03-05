# 236
# 주어진 tree에 속해있는 두 노드의 Lowest Common Ancester를 찾아라

# 풀이법1: postorder로 해당 노드들 까지의 노드 연결을 배열로 두 개 찾은 후
# 두 노드의 값들을 하나씩 체크하다가 다른 값이 나오는 순간 바로 그 전 인덱스 가 공통조상임 ex: [1,2,4] [1,2,5,7] 일때, 2가 공통 조상임

# 풀이법2: 바로 전 문제인 diameter 랑 같은 유형의 문제임
# 이 문제도 recursive postorder 로 풀 수 있음
# 포인트는 노드의 리프까지 가서 어떤 값을 부모에게 전달할지를 정하는 것. 그리고 부모의 양쪽에서 올라운 값들을 어떻게 처리할 지가 관건
# 여기서는 부모노드가 Common Ancester 노드라면 양쪽에서 두 노드가 각각 속해있음을 보고받을 것임, 이 두 값으로 공통조상 판단
# Lowest 가장 낮은 공통조상이기때문에, 노드의 리프로부터 올라오다가 최초로 발견한 그 노드가 정담임
# 사실 root는 tree의 모든 노드의 공통조상이지만 Lowest 하지는 않음

# 두 풀이법 모두 TC O(n), SC O(depth)이지만 재귀적 방법이 더 세련됨
# 풀이법 1도 구현해볼것


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



##############################################################

class LowestCommonAncestor:
  def solution(self, root: TreeNode, nodeA: TreeNode, nodeB: TreeNode) -> TreeNode:
    if root is None: 
      return 

    self._nodeA = nodeA
    self._nodeB = nodeB

    self._commonNode = None
    self._recursivePostorder(root)
    return self._commonNode
    

  def _recursivePostorder(self, node: TreeNode):
    nodeFount = 0
    leftFound = 0
    rightFound = 0
    
    if node == self._nodeA:
      nodeFount = 1
    if node == self._nodeB:
      nodeFount = 1

    if node.left:
      leftFound = self._recursivePostorder(node.left)
    if node.right:
      rightFound = self._recursivePostorder(node.right)

    sum = nodeFount + leftFound + rightFound
    if sum == 2:
      self._commonNode = node         # 한 노드가 commonNode일때 그 값을 할당해줌

    if sum > 0:               
      return 1              # 바로 위 부모 노드에게 리턴할 값
    return 0