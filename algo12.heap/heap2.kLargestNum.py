# k 번째로 큰 수 구하기

import heapq
from typing import List

def kLargest(arr: List) -> List:

  largestNums = []
  for num in arr:
    heapq.heappush(largestNums, num)
    if len(largestNums) > 3:
      heapq.heappop(largestNums)

  return largestNums