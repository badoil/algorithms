# leetcode 207

from typing import List
class HasCycle:
  def recurDFS(self, graph:List[List[int]]) -> bool:
   
    self._graph = graph
    self._seen = set()
    for idx, _ in enumerate(graph):
      loop_track = set()
      ret = self._recurDFS(idx,loop_track)
      if ret is True:
        return True   #found a cycle
        
    return False
      
  def _recurDFS(self,idx,loop_track) -> bool:
    if idx in self._seen: #visited already
      return False
    if idx in loop_track: #found a cycle
      return True
    
    loop_track.add(idx) #path add
    nexts = self._graph[idx]
    for adj_idx in nexts:  
      ret = self._recurDFS(adj_idx,loop_track)
      if ret is True:
        return True    
    loop_track.remove(idx) #path removal

    self._seen.add(idx)   #mark as visited
    return False

hasCycle = HasCycle()
hasCycle.recurDFS([[1],[],[0],[0,4],[1,6],[4],[5]])

#########################################################

class CycleDetect:
  def recurDfs(self, graph: List[List[int]]) -> bool:
    self._graph = graph
    self._seen = set()

    for idx, _ in enumerate(graph):
      loopTrack = set()
      result = self._recurDfs(idx, loopTrack)
      if result is True:
        return True

    return False

  def _recurDfs(self, idx, loopTrack) -> bool:
    if idx in self._seen:
      return False

    if idx in loopTrack:
      return True

    loopTrack.add(idx)
    nextNodes = self._graph[idx]
    for nextNode in nextNodes:
      result = self._recurDfs(nextNode, loopTrack)
      if result is True:
        return True

    loopTrack.remove(idx)
    self._seen(idx)

    return False