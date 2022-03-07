# 133
# 문제 : 주어진 Graph를 Deep Copy 하여라
# 방향이 없는 그래프임

# 링크드 리스트에서 비슷한 문제를 풀었음.(val, random 값들을 갖는 링크드 리스트 노드를 딥 카피하는 문제)
# 원본 그래프의 버텍스와 복사본을 맵핑해줘야 연결까지 복사할 수 있음
# 결국 그래프들을 모두 탐색하면서 맴핑 관계를 이용해서 복사해줘야 함
# 여기서는 BFS 로 탐색하고 해쉬맵을 이용해서 맵팽관계로 연결 해줌

from collections import deque

class Node:
  def __init__(self, val = 0):
    self.val = val
    self.adjs = []

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node0.adjs.append(node1)
node1.adjs.append(node0)
node0.adjs.append(node3)
node3.adjs.append(node0)

node1.adjs.append(node2)
node2.adjs.append(node1)
node1.adjs.append(node4)
node4.adjs.append(node1)

node2.adjs.append(node4)
node4.adjs.append(node2)
node2.adjs.append(node3)
node3.adjs.append(node2)

def cloneGraph(node: Node) -> Node:
  if node is None:
    return None  
  
  seen = set()    #for BFS
  queue = deque() #for BFS
  node_map = {}   #Mapping to new nodes
  
  seen.add(node)
  queue.append(node)
  
  while queue:
    crnt_node = queue.popleft()
    new_node = Node(crnt_node.val)  #create new node
    node_map[crnt_node] = new_node  #mapping
    
    print(crnt_node.val, end=' ')
    
    adjs = crnt_node.adjs
    for adj in adjs:
      if adj not in seen: #BFS
        seen.add(adj)
        queue.append(adj)
      
      elif adj in node_map: #edge creation 
        copy_adj = node_map[adj]
        new_node.adjs.append(copy_adj)
        copy_adj.adjs.append(new_node)

  ret_node = node_map[node]
  return ret_node




###############################################################
# BFS 탐색을 하면서 방문한 버텍스를 카피하고, 그 버텍스와 연결된 버텍스를 포문돌려서 그것이 카피된게 있으면 이를 해쉬맵에서 찾음,
# 해쉬맵에서 카피된 버텍스 찾아서 self.adjs에 연결된 노드를 저장, 이때 방향이 없는 그래프이므로 양쪽 버텍스 모두 연결
# 그리고 처음 노드와 해쉬맵에서 매핑되어 있는 노드 리턴


def pathCopy(node: Node) -> Node:
  if node is None:
    return None

  q = deque()
  visited = set()
  mapping = {}

  q.append(node)
  visited.add(node)

  while q:
    vertex = q.popleft()
    copiedVertex = Node(vertex.val)
     
    mapping[vertex] = copiedVertex    # 카피한 버텍스를 해쉬맵에 저장

    nextVertexes = vertex.adjs        # 현재 버텍스의 연결된 버텍스들, 이들을 copiedVertex에도 이 연결들을 복사해줘야함
    for next in nextVertexes:
      if next not in visited:
        q.append(next)
        visited.add(next)
      
      if next in mapping:                         # 노코프는 elif를 썻는데 if 가 맞는거 같음, mapping에 next가 있다는 뜻은 해당 버텍스가 카피가 되었다는 뜻
        nextCopiedVertex = mapping[next]          # 원본 next의 카피본인 nextCopiedVertex
        nextCopiedVertex.adjs.append(copiedVertex)   # 방향이 없는 그래프이기 때문에 연결된 양쪽 노드 모두에 대해서 연결해줘야함
        copiedVertex.adjs.append(nextCopiedVertex)
        

  return mapping[node]