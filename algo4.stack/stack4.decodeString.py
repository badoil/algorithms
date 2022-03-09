# 394
# 
# 괄호를 보자마자 스택 접근을 생각해야함

# 스택 컨셉은 간단한데 코드구현은 까다롭기에 중급
# 스택의 특성, 선입후출 구조를 잘 생각해야함.


def decodeString(s: str) -> str:
    stack = []
    num_stack = []
    
    cur_num = 0
    cur_str = ''
    for c in s:
      if c == '[':
        stack.append(cur_str)
        num_stack.append(cur_num)
        cur_str = ''
        cur_num = 0
        continue
          
      elif c == ']':          
        prev_str = stack.pop()
        num = num_stack.pop()
        cur_str = prev_str + num*cur_str
        continue
          
      if c.isdigit():
        cur_num = cur_num*10 + int(c)
      else:
        cur_str += c

    return cur_str

decodeString(s='a2[b2[ak]]')

##############################################


def decodeString(string: str) -> str:
  stack = []
  numStack = []

  tempChar = ''                     # 리턴해줄 문자열
  tempNum = 0

  for c in string:
    if c == '[':
      stack.append(tempChar)
      numStack.append(tempNum)

      tempChar = ''                 # 스택에 넣어준후 초기화 시켜줘야 '[' 이후로 해당 알파벳이 다시 안 들어감
      tempNum = 0
      continue

    elif c == ']':
      char = stack.pop()              # 괄호가 닫히면 넘버스택에 있는숫자는 이 괄호의 반복숫자에 해당하는 수고 문자스택은 이 반복하는 문자열 앞에 들어갈 문자임
      num = numStack.pop()
      tempChar = char + (tempChar*num)
      continue
      
    elif c.isdigit():
      tempNum = tempNum*10 + int(c)   # 수가 2자리 이상일 경우 이렇게 처리해야함

    else:
      tempChar += c

  return tempChar