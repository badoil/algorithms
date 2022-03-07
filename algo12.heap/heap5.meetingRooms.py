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

  

#############################################################



def meetingRooms(timeTable: List[List[int]]) -> int:
  if len(timeTable) == 0:
    return 0

  timeTable.sort(key=lambda x:x[0])

  heapLasts = []
  heapq.heappush(heapLasts, timeTable[0][1])

  roomCount = 1

  for time in timeTable[1:]:
    start = time[0]
    end = time[1]
    last = heapLasts[0]

    if last <= start:
      heapq.heappop(heapLasts)
      heapq.heappush(heapLasts, end)

    else:
      heapq.heappush(heapLasts, end)
      roomCount += 1

  return roomCount