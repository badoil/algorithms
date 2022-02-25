# 22
# 문제 : n쌍의 괄호로 만들어낼수있는 valid한 괄호 조합을 모두 return해라
# 예 : n = 2
# 답 : [“(())”,”()()”]

from typing import List

class GenParenthesis:
  def solutions(self, n: int) -> List[str]:
    open_count = n
    close_count = n
    
    self.__result = []
    self.__bt(open_count,close_count,'')
    
    return self.__result
    
  def __bt(self, open_count:int, close_count:int, letters:str ):
    if open_count == 0 and close_count == 0:
      self.__result.append(letters)
      return
    
    # open whenever we have open
    if 0<open_count:
      self.__bt(open_count-1,close_count,letters+'(')
    
    # close when we cannot open
    if open_count < close_count:
      self.__bt(open_count,close_count-1,letters+')')

gen = GenParenthesis()

gen.solutions(n=4)


##################################################################



class Parentheses:
  def solution(self, num: int) -> List[str]:
    self._open = num
    self._close = num

    self._results = []
    self._bt(self._open, self._close, '')
    return self._results

  def _bt(self, open: int, close: int, string: str):
    if open == 0 and close == 0:
      self._results.append(string)
      return

    if open > 0:
      self._bt(open-1, close, string+'(')     # 재귀호출 할 때마다 두 조건문은 항상 걸리고 그에 따라 모든 가능성들이 탐색됨

    if open < close:
      self._bt(open, close-1, string+')')     # open == close 일때 닫는 괄호는 사용 안됨
    
    