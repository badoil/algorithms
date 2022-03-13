# 78
# 문제: nums로 주어진 숫자로 만들수 있는 subsets들을 return하여라

# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.



# 함수를 재귀적으로 호출할때 value가 아니라 reference로 호출하면 메모리 낭비를 줄임
# 시간복잡도 O(n * 3의 n제곱) 이 중 3은 입력되는 정수의 갯수, n도 그 갯수임
# 공간복잡도 O(n), 각 단계마다 레터가 복사되는게 아니라 참조일 경우

# iterative로 볼 경우, 이는 dfs로 풀 수 있음
# 똑같이 스택모델을 이용하면 iterative 하게 만들 수 있음

from typing import List


class Subsets:
  def getSubsets(self, nums: List[int]) -> List[List[int]]:
    self._nums = nums
    self._subsets = []
    
    self._BT(0,[])
    
    return self._subsets
    
  def _BT(self, index :int, crnt_set : List[int]):
    if index == len(self._nums):
      self._subsets.append(crnt_set.copy())
      return
    
    num = self._nums[index]
    
    self._BT(index+1,crnt_set)
    
    crnt_set.append(num)
    self._BT(index+1,crnt_set)
    crnt_set.pop()
    
    
    
subsets = Subsets()
subsets.getSubsets(nums=[1,2,3])




############################################################



class Subset:
  def solution(self, nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
      return [[]]

    self._nums = nums
    self._results = []
    
    self._bt(0, [])
    return self._results

  def _bt(self, idx: int, crtArray: List[int]):
    if idx == len(self._nums):
      self._results.append(crtArray.copy())     # 함수를 재귀적으로 호출할 때 레퍼런스로 crtArray를 넣어주기 때문에 마지막에는 딥카피를 해줘야함. 새로운 값이기 때문
      return

    num = self._nums[idx]

    self._bt(idx+1, crtArray)   # 현재 num을 선택하지 않은 경우

    crtArray.append(num)
    self._bt(idx+1, crtArray)   # 현재 num을 선택한 경우
    crtArray.pop()