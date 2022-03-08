#leetcode 435
# 문제 : 여러 interval들이 interval[i] = [start,end] 형식으로 주어진다. interval들끼리 겹치는 구간이 존재하는데, 최소한 몇개의 interval들을 삭제하면 겹치는 구간이 사라지는가?
# 안겹치는 구간을 최소 몇개 지워야 하는가
# 이를 풀려면 한번에 글로벌 솔루션을 구하려고 해서 어렵게 느껴짐
# 하지만 이를 최대 몇개의 구간이 안겹치냐로 바꾸면, 이들 구간을 제외하고 지우면 됨
# 이렇게 구한 그리디한 방법의 솔루션이 글로벌 솔루션임이 확실하기만 하면 됨

# 응용문제로는 약속시간 잡기, 스케쥴 잡기 등등


from typing import List


def maxNonOverlapIntervals(intervals: List[List[int]]) -> int:   
  intervals.sort(key=lambda interval: interval[1])
  
  last_end = -999999  #smallest int
  interval_count = 0

  for interval in intervals:
    start = interval[0]
    end = interval[1]
    
    if start < last_end:    # 얘 불필요함
      continue
    
    if last_end <= end:   # 노코프는 여기가 end로 했는데 start 아닌지??
      interval_count += 1
      last_end = end
      
  return interval_count

print(maxNonOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))




######################################################################
# 인터벌들을 끝나는 시간 기준 정렬, 가장 먼적 끝나는 구간이 먼저 선택이 되어야 남은 공간이 많아지고
# 남은 공간이 많아야 더 많은 구간을 선택할 수 있음
# 먼저 선택이된 구간과 겹치는지 아닌지만 체크
# 안겹치면 카운트를 세주면서 진행
# 전체 인터벌 갯수 - 최대 안겹치는 인터벌 갯수 = 최소한으로 지워야하는 인터벌 갯수


# TC는 정렬 O(nlog(n)), SC는 O(1)



def minRemoveIntervals(intervals: List[List[int]]) -> int:
  if len(intervals) == 0:
    return 0


  intervals.sort(key=lambda x:x[1])

  maxCount = 0
  lastEnd = -999
  
  for interval in intervals:
    start = interval[0]
    end = interval[1]

    if start >= lastEnd:
      maxCount += 1
      lastEnd = end

  return len(intervals) - maxCount

print(minRemoveIntervals([[1,2],[2,3],[3,4],[1,3]]))