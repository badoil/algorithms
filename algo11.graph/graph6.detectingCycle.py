# 문제 : 주어진 Directed Graph에서 Cycle이 있는지 확인해보아라
# 방향성 있으면서 싸이클 있는 그래프


# 싸이클 찾기 또는 deadlock 찾기
# 방향성 없고 싸이클 있는 그래프는 DFS 로 찾는게 편함
# 방향성 있는 그래프는 싸이클이 있어도 싸이클을 발견하지 못하는 경우가 있는데 이를 해결하는 것이 이번 문제
# postOrder DFS 로 해결한다고 하지만
# 사실 내가 보기에 이 방법은 백트랙킹 방법임
# 각각의 노드에 대해서 먼저 cycle이 있는지 cycleSet에 넣으면서 먼저 체크하고 없으면 cycleSet에서 뺀다. 그리고 방문 노드로 체크
# 체크하는 과정에서 싸이클이 발견되면 True 리턴
# 여기서 방문노드체크와 cycleSet 체크 두가지가 있기 때문에, 방문노드 체크만 있을 경우 미리 방문노드로 체크되는 바람에 싸이클 체크에서 놓칠 수 있는 경우를 없애주는 것.

# 응용문제 leetcode 207 과목별 선수 과목 그래프로 표현
# 만약 여기서 선수과목의 순환이 있는지 탐지 하는 문제

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



###################################################################


class Cycle: 
  def solution(self, graph: List[List[int]]) -> bool:
    self._graph = graph
    self._visited = set()

    for idx in range(len(graph)):
      cycleTrack = set()
      result = self._recur(idx, cycleTrack)
      if result is True:
        return True

    return False
    

  def _recur(self, vertexIdx, cycleTrack) -> bool:    # cycleTrack을 가지고 가는게 중요, 이놈을 가지고 재귀적으로 호출해야 아래 싸이클 탐지 가능(아래 두번째 조건문에 걸림)
    if vertexIdx in self._visited:
      return False
    if vertexIdx in cycleTrack:
      return True

    nextVertexes = self._graph[vertexIdx] # 해당 버텍스의 다음 연결 버텍스들
    cycleTrack.add(vertexIdx)             # 해당 버텍스의 사이클 체크하기 때문에 사이클트랙에 넣어줌
    for next in nextVertexes:             
      result = self._recur(next, cycleTrack) # 해당 버텍스의 다음 연결 버텍스들이 싸이클 이루는지 재귀적으로 호출
      if result is True:
        return True
    cycleTrack.remove(vertexIdx)
    self._visited.add(vertexIdx)

    return False      # 재귀적으로 호출하다가 이도 저도 아니면(예를들어 위 두 조건문 모두 안걸리고, 다음 연결 버텍스도 없어서 포문도 돌릴일 없으면) False 리턴