# 문제: [0,1,2]만으로 구성되어있는 input 을 sort하여라

# sort 함수를 사용하면 O(nlogn) 인데 퀵소트는 O(n)으로 가능함
# idx 가 진행하는 인덱스, 교체할 인덱스들이 idx0, idx2
# 기본 아이디어는 간단함, 세개의 인덱스를 이용하는 것
# idx0, idx2 각각 처음과 끝에서 조여오면서, 진행하는 idx 해당값과 비교해서 스왑

# idx 와 idx2가 어긋나는 순간이 정렬 완료된 시점
# idx 가 하나씩 체크하면서 그 값이 0이면 idx0의 값과 바꾸고, 2이면 idx2의 값과 바꿔서 정렬
# 원소가 3개 이상이어야 가능, 포인터가 3개니까

from typing import List

def quickSort(nums: List[int]) -> List:
  idx0 = 0
  idx2 = len(nums)-1
  idx = 0

  while idx <= idx2:
    num = nums[idx]
    if num == 0:      # 진행하다보면 idx0이 가리키는 수는 0이 아닌 수에서 멈추고 idx는 1을 만나면 하나 더 진전(세번째 조건), 진행하는 idx의 해당값이 0이면 이 둘을 스왑
      nums[idx0], nums[idx] = nums[idx], nums[idx0]
      idx0 += 1
      idx += 1

    elif num == 2:    # 진행하는 idx의 해당값이 2이면, idx2 해당값과 스왑
      nums[idx2], nums[idx] = nums[idx], nums[idx2]
      idx2 -= 1

    else:
      idx += 1

  return nums

nums = [0,0,1,2,0,1,2,1,2]
quickSort(nums)