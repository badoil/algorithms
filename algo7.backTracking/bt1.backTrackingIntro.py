# 17

# 백트랙킹을 다이내믹 프로그래밍 뒤에 일부러 둔거임.
# 디피는 문제를 하위문제로 나누면서 메모이제이션으로 중복 처리를 제거해서 처리
# 비티는 모든 가능한 경우의 수, 즉  디시젼 스페이스의 가능성 모둘를 하나씩 탐색하면서 디시전 스페이스를 탐색해 나가는것
# 그 과정에서 탐색되지 않는 디시전들을 제거하고, 살아남은 디시전이 백 트랙킹. 백 트랙킹은 재귀함수의 쌓아놓은 스택이 처리되면서 그 전 스택으로 돌아가는 것을 의미
# 백 트랙킹 이후에 다시 디시전 스페이스를 탐색해 가고, 탐색 가능한 것들만 탐색해 나감
# 디시전 스페이스를 피라미드 형태로 나타낼 수 있는데, 이 형태를 재귀함수로 구현하는게 편함

# 포인트는 재귀함수의 종료조건, 재귀함수 호출, 재귀함수 호출전에 필요한 처리, 이렇게 세가지가 패턴임

# 문제: 숫자 패드로 조합할수있는 모든 문자를 return하여라

# 재귀함수를 사용, 함수호출을 할 때 매개변수의 인자가 value인지 reference인지를 상용하는 언어에 따라 정확히 사용해야함
# 시간복잡도 O(n * 3의 n제곱) 레터의 알파벳 갯수가 n이고 레터가 복사, letters 알파벳 갯수가 3일때
# 공간복잡도 O(n), 각 단계마다 레터가 복사되는게 아니라 참조일 경우

# dfs, bfs, iterative 이렇게 다른 방법으로도 풀 수 있음

from typing import List


class LetterCombinations:
  def solutions(self, digits: str) -> List[str]:
    self._keypad = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    
    if len(digits) == 0 :
      return []   
    
    self._digits = digits
    self._comb = []    
    self._BT(index=0,crntStr=[])
    return self._comb
    
  def _BT(self, index:int, crntStr: List[str]):
    if index == len(self._digits):
      comb = ''.join(crntStr)
      self._comb.append(comb)
      return
    
    num = int(self._digits[index])
    chars = self._keypad[num]
    for char in chars:
      crntStr.append(char)
      self._BT(index+1, crntStr)      
      crntStr.pop()

letterComb = LetterCombinations()
print(letterComb.solutions(digits='259'))


#################################################################################



class NumKeyPad:
  def solution(self, letters: str) -> List[str]:
    self._keypad = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

    if len(letters) == 0:
      return []

    self._count = len(letters)
    self._letters = letters
    self._results = []
    self._bt(idx=0, crtString=[])
    return self._results

  def _bt(self, idx: int, crtString: List[str]):
    if idx == self._count:
      combi = ''.join(crtString)
      self._results.append(combi)
      return

    num = int(self._letters[idx])
    chars = self._keypad[num]
    for char in chars:            # 포문은 'abc' 각 문자에 대해서 탐색. 즉 가지치기를 함. 이 중 한 문자를 선택한 상태에서(crtString으로 넣어줌) 이 과정을 또 재귀적으로 호출 
      crtString.append(char)
      self._bt(idx+1, crtString)
      crtString.pop()             # crtString에 바로 전 인덱스인 idx에 num = int(self._letters[idx]) 해당하는 캐릭터가 들어있는데, 그것이 포문 돌아갈때마다
                                  # crtString.append(char)에서 추가되기 때문에 그 전 턴에서 팝을 해줘야 함