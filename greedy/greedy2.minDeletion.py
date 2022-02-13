from typing import List

def minDeletion(s: str, costs: List) -> int:
  if len(s) <= 1:
    return 0

  lastChar = ''
  maxCost = 0
  totalCost = 0

  for idx, cost in costs:
    crtChar = s[idx]

    if lastChar != crtChar:
      lastChar = crtChar
      maxCost = cost

    else:
      if maxCost >= cost:
        totalCost += cost
      else :
        totalCost += maxCost
        maxCost = cost

  return totalCost