# 버블소팅은 O(log(n*n))으로 느린 알고리즘이라 사용하면 안됨
# 다만 버블소팅은 스테이블 소팅임
# 오름차순 정렬

# 버블소팅은 첫번째와 두번째 비교해서 큰 수를 오른쪽으로 스왑
# 두번째 세번째 비교해서 큰 수를 오른쪽으로 스왑
# 이렇게 하면 배열 내의 가장 큰 수가 맨 끝에 가게됨
# 그러면 이 젤 큰수는 더 이상 정렬할 필요가 없음

# 이름이 버블인 이유는 nums[i] 와 nums[i+1] 비교할때 이 둘이 버블처럼 묶어서 비교한다는 의미임

from typing import List

def bubbleSort(nums: List) -> List:
  for idx in range(len(nums)-1):                # idx를 빼주는 이유는, 바깥 포문이 한 턴을 돌면 가장 큰 수가 배열의 마지막 위치에 가게됨 그래서 그 값은 비교할 필요가 없어서 그럼
    for i in range(len(nums)-1-idx):            # 그래서 다음 턴의 가장 큰수는 바로전 턴의 최대값이 있는 인덱스 위치의 바로 왼쪽에 위치함
      if nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]

  return nums

print(bubbleSort(nums=[9,3,5,7,1]))

# 스테이블 소팅

def stableBubbleSort(numsString):
  for idx in range(len(numsString)-1):
    for i in range(len(numsString)-1-idx):
      if numsString[i][0] > numsString[i+1][0]:
        numsString[i][0], numsString[i+1][0] = numsString[i+1][0], numsString[i][0]

  return numsString


print(stableBubbleSort(num_strs=[(7,'a'),(5,'a'),(5,'b'),(7,'b'),(3,'c')]))

