# 23
# 문제 : k개의 정렬된 list들을 병합하여라
# k 사이즈인 민힙에 각 배열의 값들 하나씩 넣고, 팝을 하면 이 값이 젤 작은 수이고 이것들을 저장
# 팝한 수가 들어있던 배열에서 다음 수를 민힙에 넣고, 팝을 하고 저장, 이를 반복

# 어레이 챕터에 비슷한 유형 문제 있었음, 그런데 이 문제는 2개가 아니라 k개의 정렬된 배열이 주어짐
# TC는 O(nlog(k))
# SC는 민힙 유지하는 O(k)

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



####################################################################
# k 사이즈인 민힙에 각 배열의 값들 하나씩 넣고, 팝을 하면 이 값이 젤 작은 수이고 이것들을 저장
# 팝한 수가 들어있던 배열에서 다음 수를 민힙에 넣고, 팝을 하고 저장, 이를 반복
# 반복이 끝나면 저장한 결과를 리턴


def kMergeSortedArray(numArrays: List[List[int]]) -> List[int]:
  
  heap = []
  for numArray in numArrays:                                 # 처음 힙에는 각각의 배열의 (numArray[0], 0, numArray)의 형태로, k개 들어감 k = len(numArrays)
    if len(numArray) == 0:
      continue
    heapq.heappush(heap, (numArray[0], 0, numArray))
    

  results = []
  while heap:
    value, idx, numArray = heapq.heappop(heap)
    results.append(value)                             # results에는 오름차순으로 정렬된 값들이 들어가고 있음
    idx += 1
    if idx < len(numArray):
      heapq.heappush(heap, (numArray[idx], idx, numArray))    # 팝한 수가 들어있던 배열에서 다음 수를 민힙에 넣고, 팝을 하고 저장, 이를 반복

  return results