# 문제 : 미팅 스케쥴들이 intervals[i] = [start, end ] 로 주어졌다. 이때 필요한 최소 미팅룸의 갯수를 구하여라
# 미팅룸 문제로 보이지만 전형적인 인터벌 문제

# TC는 정렬 O(nlog(n)) + 힙에 추가 O(nlog(k)) 이때 log(k) 워스트 케이스 n으로 보고 O(nlog(n)), 즉 O(nlog(n)) + O(nlog(n)) = O(nlog(n)) 
# SC는 O(k) 이때 워스트 케이스이면 k = n으로 보고 O(n)

from typing import List
import heapq

def minMeetingRooms(intervals: List[List[int]]) -> int:
  if len(intervals) == 0:
    return 0
  
  intervals.sort(key = lambda interval: interval[0])    
  
  lasts = []    #min heap    
  heapq.heappush(lasts,intervals[0][1])
  
  room_count = 1
  
  for interval in intervals[1:]:
    start = interval[0]
    end = interval[1]      
    last_end = lasts[0]
    
    if last_end<=start:
      heapq.heappop(lasts)
      heapq.heappush(lasts,end)
    else:
      heapq.heappush(lasts,end)
      room_count += 1    
  
  return room_count

  
intervals = [[9,11],[9,12],[10,14],[12,16],[13,16],[15,17]]
print('min rooms : ', minMeetingRooms(intervals))




#########################################################################################################

# 시간 인터벌들을 끝나는 시간 기준 오름차순으로 정렬
# 그리고 그 처음 인터벌 한개의 끝나는 시간을 최소힙에 넣는다
# 새로운 시간의 시작 시간이 그 최소힙에 있는 끝나는 시간보다 작으면 시간이 겹치니까 새로운 룸이 필요하고 안 겹치면 그 룸 그대로 이용



def scheduling(intervals: List[List[int]]) -> int:
  if len(intervals) == 0:
    return 0

  intervals.sort(key=lambda x: x[1])    # 정렬을 해줌으로서 최소힙에서 가장 빨리 끝나는 시간하고만 비교하면 되는 것임

  minHeap = []
  heapq.heappush(minHeap, intervals[0][1])    # 최소힙에는 끝나는 시간을 넣어줌

  roomCount = 1   # 최소힙에 끝나는 시간 하나 넣었기 때문에 룸 하나 할당.
  for interval in intervals[1:]:      # 하나는 이미 넣었기 때문에 두번째 부터 시작
    startTime = interval[0]
    endTime = interval[1]
    earlyEndTime = minHeap[0]

    if earlyEndTime <= startTime:        # 새로운 시간의 시작 시간이 그 최소힙에 있는 끝나는 시간보다 크면 시간이 안 겹치니까 그 룸 그대로 이용
      heapq.heappop(minHeap)
      heapq.heappush(minHeap, endTime)
    else:                                # 새로운 시간의 시작 시간이 그 최소힙에 있는 끝나는 시간보다 작으면 시간이 겹치니까 새로운 룸이 필요
      heapq.heappush(minHeap, endTime)
      roomCount += 1                     # 새로운 룸이 필요


  return roomCount

intervals = [[9,11],[9,12],[10,14],[12,16],[13,16],[15,17]]
print('min rooms : ', scheduling(intervals))