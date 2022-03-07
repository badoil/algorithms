# k 번째로 큰 수 구하기, k번째 이상으로 큰 수들 구하기
# minHeap 이용해서 풀기
# minHeap의 사이즈를 k로 맞춤. 
# 민힙에 3을 넘어가면 그 중 가장 작은 값을 팝해서 사이즈 3을 유지
# 어떤 값이 들어와도 가장 큰 수와 그 이하 2번째 값으로 마무리됨. 이들 보다 작으면 팝되서 지워짐

# 만약 이것을 맥스힙을 이용해서 풀면
# TC는 맥스힙 만드는데 O(n) + k번 팝 하는 O(klog(n))
# SC 는 맥스힙 유지하는 O(n)
# 문제는 n이 겁나 크면 복잡도가 너무 커짐
# 이에반해 민힙은 TC는 O(nlog(k)), SC는 O(k) 


import heapq
from typing import List

def kLargest(arr: List) -> List:

  largestNums = []
  for num in arr:
    heapq.heappush(largestNums, num)
    if len(largestNums) > 3:
      heapq.heappop(largestNums)

  return largestNums