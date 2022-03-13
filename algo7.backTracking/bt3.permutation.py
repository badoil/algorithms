# 46

# 문제: nums로 주어진 숫자로 만들수 있는 모든 permutation들을 return 하여라
# 유니크한 양수만 주어짐

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.



# 재귀를 사용하는 이유는 하나의 레벨에 대한 함수 정의만 하면 되기 때문에 코드가 간결 


from typing import List

class Perm:
  def permute(self, nums: List[int]) -> List[List[int]]:

    self._nums = nums
    self._perms = []
    self._BT([])
    return self._perms  
  
  def _BT(self, crnt_sets):
    if len(crnt_sets) == len(self._nums):
      self._perms.append(crnt_sets.copy())
      return  

    for num in self._nums:
      if num in crnt_sets:
        continue
        
      crnt_sets.append(num)
      self._BT(crnt_sets)
      crnt_sets.pop()

perm = Perm()
perm.permute(nums=[1,2,3])




##############################################################################



class Permutation:
  def solution(self, nums: List[int]) -> List[List[int]]:
    
    self._nums = nums
    self._results = []

    self._bt([])
    return self._results

  def _bt(self, crtArray: List[int]):
    if len(crtArray) == len(self._nums):
      self._results.append(crtArray.copy())
      return

    for num in self._nums:
      if num in crtArray:     # 전 레벨에서 선택된 숫자는 이번에 선택될 수 없다
        continue

      crtArray.append(num)
      self._bt(crtArray)
      crtArray.pop()          # 포문이 돌아가기 때문에 팝을 해줘야함. 다음 포문에 영향을 미치지 않기 위해서

    