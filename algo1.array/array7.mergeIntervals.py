# leetcode 56

# 배열로 들어오는 겹치는 인터벌을 합쳐서 리턴, 겹치지 않으면 독립된 인터벌임
# [[1,5], [8,16], [3,7], [10,15]], 항상 그림을 그려서 아이디어를 떠올리는게 좋음
# 정렬을 안하면 O(n*n)이기 때문에 정렬 필요
# 시간복잡도는 정렬: O(log n) * O(n) -> O(nlog n)

from typing import List

def mergeIntervals(nums: List[int]) -> List:
  if len(nums) == 0:
    return

  nums.sort(key=lambda x:x[0])

  lastStartIdx = nums[0][0]
  lastEndIdx = nums[0][1]
  results = []

  for start, end in nums[1:]:
    if lastEndIdx >= start:
      lastEndIdx = end

    else:
      temp = [lastStartIdx, lastEndIdx]
      results.append(temp)

      lastStartIdx = start
      lastEndIdx = end
                                          # 바로 이전 lastStartIdx, lastEndIdx 다음 반복문 순서에서 합쳐서 리턴하는 형식이기 때문에
  temp = [lastStartIdx, lastEndIdx]        # 반복문을 다 끝나고 나면 lastStartIdx, lastEndIdx 가 남음
  results.append(temp)

  return results


mergeIntervals([[1,5], [8,16], [3,7], [10,15]])

    