# 1710

from typing import List

def maxBoxUnits(boxUnits: List[List[int]], maxBoxes: int) -> int:
  boxUnits.sort(key=lambda x:x[0], reverse=True)

  unitsCount = 0
  leftBoxes = maxBoxes
  for boxCount, units in boxUnits:
    if leftBoxes >= boxCount:
      unitsCount += (boxCount * units)
      leftBoxes -= boxCount

    else:
      unitsCount += (leftBoxes * units)
      leftBoxes -= leftBoxes

    if leftBoxes == 0:
      return unitsCount

  return unitsCount