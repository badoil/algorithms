# 정렬된 두 배열이 [1,3,5,0,0,0], [2,4,8]로 주어지고 0 자리에 오름차순 정렬된 숫자들이 들어오게 처음 배열에 합쳐줘야하는 문제
# 각 배열의 0을 제외한 원소의 갯수 m, n 이 매개변수로 주어짐
# idx1, idx2 를 서로 비교해서 큰 수를 idx0 자리 포인터에 복사함 
# 위 while 문이 끝나면 남는 [1,3,5,4,5,8] [2,4,8] -> [1,3,3,4,5,8] [2,4,8] -> [1,2,3,4,5,8] [2,4,8] 이 중 첫째배열 nums2 리턴
# 예외 케이스 배열 [4,5,6,0,0,0] [1,2,3] -> [4,5,6,4,5,6] [1,2,3] 되면서 idx1 < 0 되면서 첫번째 while 문 끝나기 때문에 두번째 while문 필요

from typing import List

def mergeTwoArraysSort(nums1: List[int], nums2: List[int], m: int, n: int) -> List:
  idx1 = m-1
  idx2 = n-1
  idx0 = len(nums1)-1

  if idx2-1 < 0:
    return

  while idx1 >= 0 and idx2 >= 0:
    num1 = nums1(idx1)
    num2 = nums2(idx2)

    if num1 > num2:
      nums1[idx0] = num1
      idx1 -= 1
      idx0 -= 1

    else:
      nums1[idx0] = num2
      idx2 -= 1
      idx0 -= 1

  while idx2 >= 0:
    num = num2[idx2]
    nums1[idx0] = num
    idx2 -= 1
    idx0 -= 1

  return nums1