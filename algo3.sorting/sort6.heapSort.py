# unstable
# 노코프는 heapify 썻지만 나는 포문 돌려서 heappush 씀, O(n)으로 동일
# n번 heappop을 하는데 O(n) * O(log n) = O(nlog n)
# 시간복잡도는 O(n) + O(nlog n) = O(nlog n)
# heapify 구현은 heap 챕터에 있음

from typing import List
import heapq


#in place memory sorting
def heapSort(nums:List[int])->List[int]:
  #python does not have maxHeap. multiply by -1
  nums = [-1*n for n in nums]
  heapq.heapify(nums)

  sorted = [0] * len(nums)
  
  for i in range(len(nums)-1,-1,-1):
    largest = -1 * heapq.heappop(nums)
    sorted[i] = largest
  return sorted

print(heapSort(nums=[3, 5, 7, 9, 4, 2]))


##################################################3

def heapSorting(nums: List[int]) -> List[int]:
  nums = [-1*num for num in nums]

  results = []
  
  for num in nums:
    heapq.heappush(results, num)

  for idx in range(len(nums)-1, -1, -1):       # n번 heappop을 하는데 O(n) * O(log n) = O(nlog n)
    largestNum = heapq.heappop(results)
    nums[idx] = -largestNum
  
  return nums

