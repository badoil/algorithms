# 692(배열이 문자열로 되어있고 리턴하는 배열값 소팅필요) 
# 347(배열이 정수, 소팅 없음)
# 문제: 주어진 list 에서 가장 많은 k개의 element를 구하여라.


# 해쉬테이블과 힙 자료구조 이용함

from typing import List
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    table = {}    
    for num in nums:
      count = table.get(num)
      if count is None:
        table[num] = 0      
      table[num] += 1
           
    #heap 
    freq_heap = []
    for num, count in table.items():
      heapq.heappush(freq_heap,(count, num))
      if k < len(freq_heap):
        heapq.heappop(freq_heap)
    
    k_freq = []
    while freq_heap:
      count , num = freq_heap[0]
      heapq.heappop(freq_heap)
      k_freq.append(num)
    k_freq.reverse()
    
    return k_freq

topKFrequent(nums=[1,1,1,1,3,3,3,5,5,2,2,4,6], k=2)




################################################################################





def topKfrequents(nums: List[int], k: int) -> List[int]:
  
  hashTable = {}
  for num in nums:                  # 해쉬에 각 수의 갯수 넣어주고
    if hashTable.get(num) is None:
      hashTable[num] = 0

    hashTable[num] += 1

  heap = []
  for num, count in hashTable.items():    # 힙큐는 원소가 들어가서 오름차순으로 정렬됨, 즉 최소힙임
    heapq.heappush(heap, (count, num))
    
  while k < len(heap):
      heapq.heappop(heap)     # 가장 많은 k개의 element를 구하면 되기에, k = len(heap)일때 멈춤, 즉 최소값이 팝되니까 남은 거는 k개만 남음

  results = []
  while heap:                           # 해당 수만 새로 배열 만들고 역순으로 정렬해서 리턴, 정렬은 문제가 요구하면 하면 됨
    count, number = heapq.heappop(heap)
    results.append(number)

  results.reverse()
  return results

topKfrequents(nums=[1,1,1,1,3,3,3,5,5,2,2,4,6], k=2)