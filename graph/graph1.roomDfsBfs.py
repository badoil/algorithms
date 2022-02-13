# leecode 841

from typing import List
from collections import deque

class dfsBfs:
  def recurDfs(self, rooms: List[List[int]]) -> bool:
    self._rooms = rooms
    self._seen = set()

    
    self._rucurDfs(0)

    if len(self._rooms) == len(self._seen):
      return True
    else:
      return False

  def _recurDfs(self, roomIdx: int) -> None:
    print(roomIdx, end=' ')
    self._seen.add(roomIdx)

    keys = self._rooms[roomIdx]
    for key in keys:
      if key not in self._seen:
        self._recurDfs(key)


  def iterDfs(self, rooms:List[List[int]]) -> bool:
    seen = set()
    stack = []

    seen.add(0)
    stack.append(0)
    print(0, end=' ')

    while stack:
      roomIdx = stack.pop()
      keys = rooms[roomIdx]
      for key in keys:
        if key not in seen:
          stack.append(key)
          seen.add(key)
          print(key, end=' ')

    if len(seen) == len(rooms):
      return True
    else:
      return False


  def iterBfs(self, rooms: List[List[int]]) -> bool:
    seen = set()
    queue = deque()

    seen.add(0)
    queue.append(0)
    print(0, end=' ')

    while len(queue) > 0:
      roomIdx = queue.popleft()
      keys = rooms[roomIdx]
      for key in keys:
        if key not in seen:
          seen.add(key)
          queue.append(key)
          print(key, end=' ')

    if len(rooms) == len(seen):
      return True
    else:
      return False
