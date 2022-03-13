# 131
# 문제 : 주어진 string을 palindromic한 알파벳들로 쪼개라 
# 예 : s = aabb 
# 답 : [['a', 'a', 'b', 'b'], ['a', 'a', 'bb'], ['aa', 'b', 'b'], ['aa', 'bb']]

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]
 
# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.

# s = aaabb
# a|aabb, aa|abb, aaa|bb, aaab|b, aaabb| 이때 네번째(aaab|b), 다섯번째(aaabb|)의 aaab와 aaabb는 palindrome 아니므로 제외
# 이때 두번째 aa|abb를 보면 abb에 대해서
# a|bb, ab|b, abb| 로 나뉘고 이 중 첫번째 a 만 palindrome 이므로 bb에 대해서
# b|b, bb| 로 나뉜다
# [aa, a, b, b]와 [aa, a, bb] 가 palindrome 인 경우를 구할 수 있음


from typing import List

class PalindromePartition:
  def find_solutions(self, s: str) -> List[List[str]]:
    if len(s) == 0:
      return []
    
    self.__s = s    
    self.__results = [] 
  
    for idx in range(0,len(s)):
      self.__bt(0,idx,[])    
    
    return self.__results
    
  def __is_palindrome(self,begin:int,last:int) -> bool:
    while(begin<last):
      if self.__s[begin] != self.__s[last]:
        return False      
      begin += 1
      last -= 1
    return True
    
    
  def __bt(self, begin:int, last:int, letters : List[str]):
    is_palindrome = self.__is_palindrome(begin,last)
    #exit conditions
    if not is_palindrome:
      return
    
    letters.append(self.__s[begin:last+1])
    if len(self.__s) == last+1:
      self.__results.append(letters.copy())
      letters.pop()
      return    
    
    #recursive calls
    for idx in range(last+1,len(self.__s)):
      self.__bt(last+1,idx,letters)
    
    letters.pop()
    return


partition = PalindromePartition()

partition.find_solutions(s="aabb")
[['a', 'a', 'b', 'b'], ['a', 'a', 'bb'], ['aa', 'b', 'b'], ['aa', 'bb']]





#################################################################################