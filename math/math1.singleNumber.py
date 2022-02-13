from typing import List

#배열안의 숫자중에 중복되지 않는 한개의 수를 리턴하는 문제
#hashMap Approach
def singleNumber(nums: List[int]) -> int:
  hashSet = set()

  for num in nums:
    if num in hashSet:
      hashSet.remove(num)

    else:
      hashSet.add(num)

  result = hashSet.pop()
  return result


def singleNumberByBit(nums: List[int]) -> int:
  result = 0
  for num in nums:
    result ^= num

  return result