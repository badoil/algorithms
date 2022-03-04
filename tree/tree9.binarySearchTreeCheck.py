# 98
# 주어진 Binary Tree가 BST인지 체크하여라
# O(n) 으로 풀려면, 각 노드를 체크할때 바운딩(범위 a < x < y)를 업데이트하면서 체크하면됨
# 이거를 iterative 하게도 풀어봐라

# binary search tree
# 자기보다 작은 수를 갖는 노드는 왼쪽에, 큰 수를 갖는 노드는 오른쪽에 정력해놓은 노드 트리
# 어떤 수를 찾을때 노드 기준으로 왼쪽 또는 오른쪽으로 이동하면서, 해당 수를 쉽고 빠르게 검색
# TC, O(log(n))<= O(depth) <= O(n): 최선의 경우에 full binary tree 이면 depth 가 log(n) 이고 최악의 경우에 오른쪽(왼쪽) 자식만 있는경우 n
# find: 해당 값을  O(depth) 로 찾음
# insert: 해당 값이 들어갈 장소를 O(depth) 로 찾음
# delete: 해당 값이 리프이면 O(depth) 로 찾아서 지움
#         해당값이 1개의 자식노드가 있으면, 해당 노드 지우고 그대로 자식노드를 부모노드와 연결
#         해당값이 2개의 자식노드가 있으면, 왼쪽에서 가장 쿤수나 오른쪽에서 가장 작은수를 해당노드와 치환

# 바이너리 서치 트리는 최선의 경우 위의 동작들을 O(log(n))으로 수행하기 때문에 쓰는거임


from collections import deque
import math

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(8)
node3 = TreeNode(3)
node10 = TreeNode(10)
node1 = TreeNode(1)
node6 = TreeNode(6)
node14 = TreeNode(14)
node4 = TreeNode(4)
node7 = TreeNode(7)
node13 = TreeNode(13)

root.left = node3
root.right = node10

node3.left = node1
node3.right = node6

node10.right = node14

node6.left = node4
node6.right = node7

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

treeLevelPrint(root)

def isBST(root: TreeNode) -> bool:

  def recurIsBST(node, min: int, max: int) -> bool:
    if node is None:
      return True

    value = node.val
    if value <= min:
      return False

    if max <= value:
      return False

    left_ret = recurIsBST(node.left, min, value)
    right_ret = recurIsBST(node.right, value, max)

    return left_ret and right_ret


  ret = recurIsBST(root, -math.inf, math.inf)
  return ret

print(isBST(root))

###############################


def bst(root: TreeNode) -> bool:
  def _recur(node, min: int, max: int) -> bool:
    if node is None:
      return None

    val = node.val
    if min >= val:
      return False
    if max <= val:
      return False

    left = self._recur(node.left, min, val)
    right = self._recur(node.right, val, max)

    return left and right

  result = _recur(root, -math.inf, math.inf)
  return result