# 74 sorted2DArrayMatrix

# 정렬된 2차원 배열 매트릭스에서 주어진 값을 찾는 문제,
# 정렬이 list[0][0]부터 list[m][n]까지 오르차순으로 되어 있는 경우
# 각 행들과 열이 따로따로 오름차순으로 정렬되어 있는 경우가 있을 수 있음
# 두번째 경우를 풀어보자
# 그림을 그려야함

# 피봇을 nums[pivotRowIdx, 0]부터 시작할때
# 이 값이 타겟값보다 작으면 오름차순으로 정렬된 그 값이 포함된 행에는 해당 값이 당연히 없으므로 이 행을 지운다고 생각하고 pivotColIdx +1 해줌
# 이런식으로 반복하면 target == pivot 이 참인 값을 만나면 그 인덱스들을 리턴

from typing import List

def twoDmatrix(nums: List[List[int]], target: int) -> List:
  rowCount = len(nums)
  colCount = len(nums[0])

  pivotRowIdx = rowCount - 1
  pivotColIdx = 0
  for _ in range(rowCount+colCount-1):
    if pivotRowIdx < 0 or pivotColIdx< 0 or pivotRowIdx >= rowCount or pivotColIdx >= colCount:  # 매트릭스에 없는 값이 타겟일때 매트릭스를 벗어난 인덱스 값이 pivotRowIdx, pivotColIdx 에 들어갈 수 있음
      return -1
    if nums[pivotRowIdx][pivotColIdx] == target:
      return [pivotRowIdx, pivotColIdx]

    elif nums[pivotRowIdx][pivotColIdx] < target:
      pivotColIdx += 1

    elif nums[pivotRowIdx][pivotColIdx] > target:
      pivotRowIdx -= 1

  return -1

twoDmatrix([[1,3,5,7], [2,8,11,12], [4,9,14,19], [6,15,25,40]], 22)