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


  #############################################

def copyPath(node: Node) -> Node:
    if node is None:
      return None

    seen = set()
    queue = deque()
    hashMap = {}

    seen.add(node)
    queue.append(node)

    while queue:
      crtNode = queue.popleft()
      newNode = Node(crtNode.val)
      hashMap[crtNode] = newNode

      connNodes = crtNode.conn
      for connNode in connNodes:
        if connNode not in seen:
          seen.add(connNode)
          queue.append(connNode)
        
        elif connNode in hashMap:
          copyNode = hashMap[connNode]
          newNode.conn.append(copyNode)
          copyNode.conn.append(newNode)

    copyNode = hashMap[node]
    return copyNode
