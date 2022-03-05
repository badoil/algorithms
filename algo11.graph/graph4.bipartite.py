from typing import List

def isBipartiteDFS(graph: List[List[int]]) -> bool:
  vertex_num = len(graph)
  colors = [0] * vertex_num       #0:None, 1:GroupA, -1:GroupB 
  seen = set()
      
  for start_idx in range(vertex_num):
    if start_idx in seen:
      continue
    
    stack = []
    stack.append(start_idx)
    seen.add(start_idx)
    colors[start_idx] = 1
    
    while stack:
      idx = stack.pop()
      conn_idxs = graph[idx]
      color = colors[idx]

      for conn_idx in conn_idxs:
        if conn_idx not in seen:
          seen.add(conn_idx)
          stack.append(conn_idx)
          colors[conn_idx] = -1 * color
          continue

        if colors[conn_idx] * color != -1:
          return False
      
  return True

print(isBipartiteDFS([[1,3],[0,2],[1,3],[0,2]]))
print(isBipartiteDFS([[1,2,3],[0,2],[0,1,3],[0,2]]))


###########################################################

def bipartite(graph: List[List[int]]) -> bool:
  vortexNum = len(graph)
  colors = [0] * vortexNum
  
  seen = set()
  stack = []

  for idx in range(vortexNum):
    if idx in seen:
      continue

    stack.append(idx)
    seen.add(idx)
    colors[idx] = 1

    while stack:
      idx = stack.pop()
      connectingIdxs = graph[idx]
      color = colors[idx]

      for connectingIdx in connectingIdxs:
        if connectingIdx not in seen:
          stack.append(connectingIdx)
          seen.add(connectingIdx)
          colors[connectingIdx] = -1 * color
          continue

        if colors[connectingIdx] * color != -1:
          return False

  return True