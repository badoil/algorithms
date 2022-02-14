# 20, 1249(중급) 풀어보기
# stack 전용 자료구조 말고 배열 사용해서 할 수 있음

# 이 문제는 주어진 '{([{}]())}' 이런 문자열이 모두 닫히는 괄호인지 참, 거짓 리턴


class ValidParentheses:  
  def _matchCh(self, c: str) -> str:
    if c == ')':
      return '('
    elif c == '}':
      return '{'
    elif c == ']':
      return '['
      
  def isValid(self, s: str) -> bool:    
    stack = []    
    for ch in s:
      if len(stack) == 0:
        stack.append(ch)
      elif ch == '(' or ch == '{' or ch == '[':
        stack.append(ch)
      else: 
        match_ch = self._matchCh(ch)
        last_ch = stack[-1]
        if match_ch == last_ch:
          stack.pop()
        else:
          return False      
      
    if len(stack) == 0:
      return True
    else:
      return False

vp = ValidParentheses()
vp.isValid(s='{([{}]())}')

#########################################



class Parenteses:
  def _match(self, char: str) -> str:
    if char == ')':
      return '('

    elif char == ']':
      return '['

    elif char == '}':
      return '{'

  
  def valid(self, string: str) -> bool:
    stack = []
    for c in string:
      if len(stack) == 0:
        stack.append(c)

      elif c == ')' or c==']' or c=='}':
        matchChar = self._match(c)
        lastChar = stack[-1]
        if matchChar == lastChar:          # 스택의 마지막 알파벳이 닫으려는 지금 괄호와 짝이 맞아야 팝을 할 수 있음
          stack.pop()
        else:
          return False

      else:
        stack.append(c)


    if len(stack) == 0:
      return True
    else:
      return False