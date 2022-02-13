# leetcode 347
# 692, 973 비슷한 유형의 문제

from typing import List
import heapq
from collections import defaultDict


def topKFrequent(nums: List[int], k: int) -> List[int]:
  if k == 0:
    return []
  
  #hash map
  count_map = defaultdict(int)
  
  #count over nums
  for num in nums:
    count_map[num] += 1
  
  #fixed size heap
  topK_heap = []
  for num in count_map:
    heapq.heappush(topK_heap,(count_map[num],num))  #use hashmap count as comp
    if k < len(topK_heap):
      heapq.heappop(topK_heap)
      
  #return list
  topK = []
  for count,num in topK_heap:
    topK.append(num)
    
  return topK


topK = topKFrequent(nums=[1,3,5,3,9,3,7,5], k = 2 )
print(topK)

########################################################################

def kFrequentElems(arr: List, k: int) -> List:

  hashNum = defaultDict(int)
  for num in arr:
    hashNum[num] += 1

  largestNums = []
  for num in arr:
    heapq.heappush(largestNums, (hashNum[num], num))
    if len(largestNums) > k:
      heapq.heappop(largestNums)

  results = []
  for count, num in largestNums:
    results.append(num)

  return results