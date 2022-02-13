from typing import List
import heapq

def mergeKsortedLists(lists: List[List[int]]):
  merged_list = []
  heap = []

  for nth_list in lists:
    if len(nth_list) == 0:
      continue
    
    #heap push ( num, idx, list)
    heapq.heappush(heap,(nth_list[0],0,nth_list))

  while heap:
    num, idx, nth_list = heapq.heappop(heap)
    merged_list.append(num)
    idx += 1
    if idx < len(nth_list):
      heapq.heappush(heap,(nth_list[idx], idx, nth_list))

  return merged_list


lists = [[1,5,7,9],[2,6,8],[3,4,10]]

print(mergeKsortedLists(lists))


###################################################


def mergeSortedArrays(graph: List[List[int]]) -> List:
  
  sortedArray = []
  heap = []
  for array in graph:
    if len(array) == 0:
      continue

    heapq.heappush(heap, (array[0], 0, array))

  while heap:
    num, idx, array = heapq.heappop(heap)
    sortedArray.append(num)

    idx += 1
    if len(array) > idx:
      heapq.heappush(heap, (array[idx], idx, array))

  return sortedArray