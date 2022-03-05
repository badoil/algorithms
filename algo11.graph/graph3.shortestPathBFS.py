from typing import List
from collections import deque

class ShortestPath:
  def BFS(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    if rows == 0:
      return -1
    
    cols = len(grid[0])
    if cols == 0:
      return -1
    
    if grid[0][0] != 0:
      return -1
    
    self._rows = rows
    self._cols = cols
    self._grid = grid
    
    queue = deque()
    countQ = deque()
    seen = set()
    queue.append((0,0))
    countQ.append(1)
    seen.add((0,0))
    
    while queue:
      y, x = queue.popleft()
      count = countQ.popleft()
      self._grid[y][x] = count
      
      if y == self._rows-1 and x == self._cols-1:
        return count
      
      idx_pairs = [[y-1,x-1],[y-1,x],[y-1,x+1],[y,x+1],[y+1,x+1],[y+1,x],[y+1,x-1],[y,x-1]] #index candidates
      idx_pairs = list(filter(self._filter, idx_pairs)) #filtering
      
      for idx_pair in idx_pairs:
        next_y, next_x = idx_pair
        if (next_y, next_x) not in seen:
          queue.append((next_y, next_x))
          countQ.append(count+1)
          seen.add((next_y, next_x))
          
    return -1
          
          
  def _filter(self, idx2d ) -> bool:
    y, x = idx2d
    if y<0 or x<0 or self._rows<=y or self._cols<= x:
      return False    
    elif self._grid[y][x] == 0:
      return True
    return False
      
      
stp = ShortestPath()

matrix = [[0,1,0,0,0],[0,1,0,0,0],[1,0,0,1,0],[0,0,1,1,0]]

print(stp.BFS(matrix))

###############################


class ShortestPath:
  def bfs(self, grid: List[List[int]]) -> int:
    row = len(grid)
    if row == 0:
      return -1

    col = len(grid[0])
    if col == 0:
      return -1

    if grid[0][0] == 1:
      return -1

    self._row = row
    self._col = col
    self._grid = grid

    queue = deque()
    qCount = dueque()
    seen = set()

    queue.append((0,0))
    qCount.append(0)
    seen.add((0,0))

    while queue:
      y, x = queue.popleft()
      count =  qCount.popleft()
      self._grid[y][x] = count

      if y == self.row-1 and x == self.col-1:
        return count

      nextIdxes = [[y-1,x-1],[y-1,x],[y-1,x+1],[y,x+1],[y+1,x+1],[y+1,x],[y+1,x-1],[y,x-1]]
      nextIdxes = list(filter(self._filter, nextIdxes))
      # nextIdxes = [x for x in nextIdxes if self._filter(x)]
      for nextIdx in nextIdxes:
        y, x = nextIdx
        if (y,x) not in seen:
          queue.append((y, x))
          qCount.append(count+1)
          seen.add((y, x))
    
    return -1

  def _filter(self, nums: List):
    y, x = nums
    if y < 0 or x < 0 or self._row >= y or self._col >= x:
      return False
    elif self._gird[y][x] == 0:
      return True
    return False