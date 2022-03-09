# 394
# 문제: s 로 주어진 계산식을 계산하여라
# 'b2[ak]' : 'ak'가 2번 반복되고 'b'가 그 앞에 붙는 'bakak' 리턴해야함
# 괄호 안에 문자를 앞에 숫자만큼 반복하고 'b'는 앞에 붙는 거임

# 괄호를 보자마자 스택 접근을 생각해야함

# 스택 컨셉은 간단한데 코드구현은 까다롭기에 중급
# 스택의 특성, 선입후출 구조를 잘 생각해야함.

# 'a2[b2[ak]]' 이런건 쉬운데, '23[a]100[def]42[b]' 이런경우 23을 처리하기 까다로움


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
'abakakbakak'

decodeString(s='23[a]100[def]42[b]')
'aaaaaaaaaaaaaaaaaaaaaaadefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefdefbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'




#################################################################################
# 'a2[b2[ak]]' 이런건 쉬운데, '23[a]100[def]42[b]' 이런경우 23을 처리하기 까다로움

# b2[ak] 같은 경우 'bakak'를 구해야함
# 포인트는 b2[ak] 같은 경우 괄호가 시작할때('[') stack, numStack에 각각 'b', 2 를 넣고
# 'a', 'k'는 tempChar에 넣어서 'ak' 를 만듬
# 그리고 괄호가 끝날때 (']') tempChar에 'ak'가 numStack에 들어있는 2번 반복하고 그 앞에 stack에 들어있는 'b'가 붙어야 함
# stack.pop() + (tempChar * numStack.pop()) == 'b' + ('ak' * 2) == 'b' + 'akak' == 'bakak'
# 이를 반복



def decodeString(string: str) -> str:
  stack = []
  numStack = []

  tempChar = ''                     # 리턴해줄 문자열
  tempNum = 0

  for c in string:
    if c == '[':                    # 괄호가 시작되면 괄호 전의 문자와 숫자를 각각 stack, numStack에 넣어준다, 나중에 이 괄호가 닫힐때 이 괄호안에 문자열이 몇번 반복되고, 그 앞에 붙을 문자는 무엇인지 결정하기 위해
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