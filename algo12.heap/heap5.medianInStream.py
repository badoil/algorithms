# 295
# 문제 : Data Stream에서 median 을 찾는 class를 만들어라
# median 이란 오름차순으로 정렬된 배열의 중간 인덱스에 해당하는 값을 말한다
# 배열의 갯수가 홀수면 중간 인덱스 값이고, 짝수면 배열을 반으로 나눠서 왼쪽 배열의 마지막 값과 오른쪽 배열의 처음 값을 더해서 2로 나눈 값

# 이 문제는 새로운 수가 배열에 추가될 때마다 정렬을 해줘야하기 때문에 O(nlog n)
# 만약 이 정렬을 안해도 된다면 시간복잡도 줄일 수 있을것
# 포인트는 배열의 중간값 이외에는 정렬이 되든 말든 상관없다는 것. 즉 중간값만 정확하게 그 배열의 중간에 있으면 되는것
# 이때 배열을 왼쪽으로는 maxHeap 오른쪽으로는 minHeap 배열로 나눈다고 생각해보자, 즉 전체 배열에서 작은 수들은 왼쪽(maxHeap), 큰 수들은 오른쪽(minHeap)
# 이렇게 하면 작은수 중에 젤 큰수가 루트, 큰 수들 중에 젤 작은수가 루트가 되서, 전체 배열에서 그 두가 중간으로 모이는 것

# 두 배열의 길이 합이 홀수이면 더 긴 힙의 배열의 루트가 median 임.
# 이 두 배열의 길이가 2 이하로 차이나게 조정하면서, 길이가 1 더 긴 배열의 루트 노드 값이 median 이다.

# 이때 추가하는 수가 미디언 보다 크면 큰수이기 때문에 minHeap, 작으면 작은수라 maxHeap 에 추가한다
# 추가면서 2 이상 차이가 나면 더 긴 배열에서 팝한 후 다른 배열로 넣어줘야 중간 값이 가운데로 모이는 배열을 유지 할 수 있음


import heapq

class MedianFinder:
  def __init__(self):
    self._maxHeap = []
    self._minHeap = []


  def addNum(self, num: int) -> None:
    if len(self._minHeap) == 0 and len(self._maxHeap) == 0:
      heapq.heappush(self._minHeap,num)
      return

    median = self.findMedian()
    if median < num:
      heapq.heappush(self._minHeap,num)
    else:
       heapq.heappush(self._maxHeap,-1 * num)

    if len(self._maxHeap) + 1 < len(self._minHeap):
      pop_num = heapq.heappop(self._minHeap)
      heapq.heappush(self._maxHeap,-1 * pop_num)  #python does not support max heap
      
    elif len(self._minHeap) + 1 <  len(self._maxHeap):
      pop_num = -1 * heapq.heappop(self._maxHeap)
      heapq.heappush(self._minHeap,pop_num)
    
  def findMedian(self) -> float:    
    if  len(self._minHeap)<len(self._maxHeap):
      small_med = -1 * self._maxHeap[0]
      return small_med
    elif len(self._maxHeap)<len(self._minHeap):
      large_med = self._minHeap[0]
      return large_med
    else:
      small_med = -1 * self._maxHeap[0]
      large_med = self._minHeap[0]
      med = (small_med + large_med)/2
      return med

  def clear(self) -> None:
    self._maxHeap.clear()
    self._minHeap.clear()

  
median_finder = MedianFinder()

median_finder.clear()
median_finder.addNum(1)
print("[1]", "median: ", median_finder.findMedian())
median_finder.addNum(3)
print("[1,3]", "median: ", median_finder.findMedian())
median_finder.addNum(5)
print("[1,3,5]", "median: ", median_finder.findMedian())
median_finder.addNum(5)
print("[1,3,5,5]", "median: ", median_finder.findMedian())
median_finder.addNum(4)
print("[1,3,5,5,4]", "median: ", median_finder.findMedian())
median_finder.addNum(8)
print("[1,3,5,5,4,8]", "median: ", median_finder.findMedian())
median_finder.addNum(5)
print("[1,3,5,5,4,8,5]", "median: ", median_finder.findMedian())
median_finder.addNum(1)
print("[1,3,5,5,4,8,5,1]", "median: ", median_finder.findMedian())
median_finder.addNum(2)
print("[1,3,5,5,4,8,5,1,2]", "median: ", median_finder.findMedian())


# [1] median:  1
# [1,3] median:  2.0
# [1,3,5] median:  3
# [1,3,5,5] median:  4.0
# [1,3,5,5,4] median:  4
# [1,3,5,5,4,8] median:  4.5
# [1,3,5,5,4,8,5] median:  5
# [1,3,5,5,4,8,5,1] median:  4.5
# [1,3,5,5,4,8,5,1,2] median:  4



#############################################################################



class Median:
  def __init__(self):
    self.minHeap = []
    self.maxHeap = []

  def add(self, num: int) -> None:
    if len(self.minHeap) == 0 and len(self.maxHeap) == 0:
      heapq.heappush(self.minHeap, num)
      return

    medianNum = self._findMedian()
    if num > medianNum:
      heapq.heappush(self.minHeap, num)

    elif num < medianNum:
      heapq.heappush(self.maxHeap, -num)

    if len(self.minHeap)+1 < len(self.maxHeap):
      popNum = heapq.heappop(self.maxHeap) * -1
      heapq.heappush(self.maxHeap, popNum)

    elif len(self.maxHeap)+1 < len(self.minHeap):
      popNum = heapq.heappop(self.minHeap) * -1
      heapq.heappush(self.maxHeap, popNum)

    
  def _findMedian(self) -> float:
    if len(self.minHeap) > len(self.maxHeap):
      popNum = heapq.heappop(self.minHeap)
      return popNum

    elif len(self.minHeap) < len(self.maxHeap):
      popNum = heapq.heappop(self.maxHeap) * -1
      return popNum

    else:
      minNum = heapq.heappop(self.minHeap)
      maxNum = heapq.heappop(self.maxHeap) * -1
      medianNum = (minNum+maxNum)/2
      return medianNum

  def clear(self) -> None:
    self.minHeap.clear()
    self.maxHeap.clear()