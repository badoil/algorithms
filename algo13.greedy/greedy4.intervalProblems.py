#leetcode 435
# 안겹치는 구간이 몇개인가
from typing import List


def maxNonOverlapIntervals(intervals: List[List[int]]) -> int:   
  intervals.sort(key=lambda interval: interval[1])
  
  last_end = -999999  #smallest int
  interval_count = 0

  for interval in intervals:
    start = interval[0]
    end = interval[1]
    
    if start < last_end:
      continue
    
    if last_end <= end:   # 노코프는 여기가 end로 했는데 start 아닌지??
      interval_count += 1
      last_end = end
      
  return interval_count

print(maxNonOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

  ###########################################################

def nonOverlappingIntervals(intervals: List) -> int:
  if len(intervals) == 0:
    return 0

  intervals.sort(key=lambda x:x[1])

  last = -99999
  intervalCount = 0
  for interval in intervals:
    start = interval[0]
    end = interval[1]

    if last > start:
      continue
    
    if last <= start:
      intervalCount += 1
      last = end

  return intervalCount


