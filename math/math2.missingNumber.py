from typing import List

# 연속된 정수에서 빠진 하나의 수를 리턴해라

def missingByHash(nums: List[int]) -> int:
  hashSet = set()

  count = len(nums)
  for num in range(count+1):
    hashSet.add(num)

  for num in nums:
    if num in hashSet:
      hashSet.remove(num)

  result = hashSet.pop()
  return result

def missingByFormula(nums: List[int]) -> int:
  count = len(nums)
  total = (count*count+1)/2
  for num in nums:
    total -= num

  return total


def missingByBit(nums: List[int]) -> int:
  count = len(nums)
  total = 0
  for num in range(count+1):
    total ^= num

  for num in nums:
    total ^= num

  return total