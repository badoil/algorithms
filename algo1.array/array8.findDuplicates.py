# 287

# 주어진 배열의 1~i 로 이루어져있을때 [1,2,3,4,5,2] 이런식으로 2가 한번더 들어가 있는경우 그 2를 리턴해야함 
# 정렬을 하고 다른 배열 메모리를 만들어서 하나씩 체크해나가면 시간복잡도 O(nlog n), 공간복잡도 O(n) 이 필요
# 하지만 입력된 배열 자체를 메모리로 사용하고 배열의 원소 자체를 인덱스로 본다면 시간복잡도 O(n), 공간복잡도 O(1) 으로 가능
# 해당 인덱스의 원소값에 음수로 체크, 중복된 수는 이미 그 인덱스 값이 음수일 것이기 때문에 바로 그 값을 리턴

from typing import List

def findDuplicate(nums: List) -> int:
  if len(nums) == 0:
    return None

  for num in nums:
    elem = nums[num]
    if elem < 0 :        #주어진 배열은 양의 정수만 있는것
      return -elem
    nums[num] = -elem

  return 0


findDuplicate([1,2,3,4,5,2])