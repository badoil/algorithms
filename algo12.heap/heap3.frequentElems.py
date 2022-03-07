# leetcode 347
# 문제 : 주어진 array에서 가장 많이 나타나는 숫자 K개를 찾아라. K = 2
# TC는 O(n + mlog(k)) 이때 log(k) 상수로 보고 O(n + m) 이때 m<=n 이므로 n으로 보고 O(n + n), 즉 O(n)
# SC는 O(m + k) 이때 k를 상수로 보고 O(m), 이때 m<=n 이므로 n으로 보고 O(n)


# 692, 973 비슷한 유형의 문제

from typing import List
import heapq
from collections import defaultDict


def topKFrequent(nums: List[int], k: int) -> List[int]:
  if k == 0:
    return []
  
  #hash map
  count_map = defaultdict(int)    # 키에 대한 밸류를 지정하지 않으면 디폴트로 0이 들어감
  
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
# {num1: count1, num2: count2} 형태로 해쉬맵을 만들고
# [(count1, num1), (count2, num2)] 원소가 들어가는 민힙을 만듬
# 민힙을 이용해서 k개를 유지하면서 팝을 해주면, 남는 건 제일 큰 k개의 원소들임, 그 원소들보다 작은 애들은 계속 팝이 되서 사라지기 때문

def kFrequentNumbers(nums: List[int], k: int) -> List[int]:
  if k == 0:
    return []

  hashMap = {}              # {num: count} 형태로 해쉬맵을 만듬 
  for num in nums:          # 노코프처럼 defaultdict(int) 쓰면 코드가 더 간단해짐
    if num in hashMap:
      count = hashMap[num]
      hashMap[num] = count+1
    else:
      hashMap[num] = 1
  
  print('hashMap', hashMap)


  minHeap = []            # 민힙을 이용해서 k개를 유지하면서 팝을 해주면, 남는 건 제일 큰 k개의 원소들임, 그 원소들보다 작은 애들은 계속 팝이 되서 사라지기 때문
  for num in hashMap:
    heapq.heappush(minHeap, (hashMap[num], num))    # 이때 (count, num) 민힙은 num을 기준으로 만들어짐
    if len(minHeap) > k:
      heapq.heappop(minHeap)

  results = []
  for count, num in minHeap:      # 제일 큰 count를 갖는 num을 뽑아내는 작업
    results.append(num)

  return results

topK = kFrequentNumbers(nums=[1,3,5,3,9,3,7,5], k = 2 )
print(topK)