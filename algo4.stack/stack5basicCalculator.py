# 227
# 문제: 숫자 계산식으로 이루어진 str을 decoding 해서 return 하여라
# 문자열로 주어진 계산을 숫자처럼 계산하기

# 스택이 어려운 이유는 포문과 함께 현재 순번과 이전 순번을 이용하고
# 거기에 배열의 인덱스, 인덱스에 해당하는 값을 이용해서임
# 이것들에 익숙해져야함


def calculate(s: str) -> int:
    s+='+' #additional last op
    stack = [] # 7 -6 
    
    cur_num = 0  # 7 0 6 3
    prev_op = '+' # - /
    for c in s:
      if c.isdigit():
        cur_num = cur_num*10 + int(c)
        
      elif c == ' ':
        continue     
              
      else: #ops
        if prev_op == '+':
          stack.append(cur_num)

        elif prev_op == '-':
          stack.append(-cur_num)
          
        elif prev_op == '*':
          stack[-1] = stack[-1]*cur_num      

        elif prev_op == '/':
          stack[-1] = int(stack[-1]/cur_num)

        cur_num = 0
        prev_op = c
        
    return sum(stack)


calculate(s='7 - 6 / 3 + 3 * 2 + 4')



##########################################################################
# 포인트는 스택에 음수와 양수를 계속 넣다가 마지막에 sum(stack) 함수로 계산하면 끝나는거임
# 따라서 곱셈 나눗셈은 바로바로 계산해줘야 함

# 이를 위해서 숫자는 그 수 앞의 '+', '-' 부호에 의해 음수나 양수가 정해짐
# 이때 포인트는 부호가 현재 문자라면 이를 prev_op = c 넣기만 하고, 부호 다음에 나오는 숫자문자열에 prevOp 붙여서 crtNum에 저장
# 그리고 다음 부호가 현재 문자열일때 위의 crtNum을 스택에 넣어줌
# 앞의 부호에 따라 음수나 양수를 결정해주고 이 수들을 스택에 넣어주는 것임

# 곱셈, 나눗셈은 부호가 나오면 stack[-1] 있는 수와 현재 수를 이용해서 계산한 후, 스택에 그 결과값 저장
# 이때 '3 * 2 + 4' 이런 계산식에서 3*2가 계산되는 순간은 현재 문자열이 '+'일때, stack[-1]=3, prevOp= '*', crtNum에=2, 가 되어서 계산되는 것임
# 반복문 끝나면 스택에 있는 수 계산sum(stack)

calculate(s='7 - 6 / 3 + 3 * 2 + 4')



def calculation(s: str) -> int:
  s += '+'       # 이게 없으면 마지막 숫자가 스택에 안들어감, 왜냐하면 crtNum은 현재 문자열 c가 부호일때 prevOp을 달고 스택에 들어감
  stack = []

  crtNum = 0
  prevOp = '+'

  for c in s:
    if c.isdigit():
      crtNum = crtNum*10 + int(c)

    elif c == ' ':
      continue


    else:                     # 첫번째 수 7이 crtNum일때 '-'부호가 c이고, prevOp == '+' 이기에 숫자가 들어감
      if prevOp == '+':
        stack.append(crtNum)

      elif prevOp == '-':
        stack.append(-crtNum)

      elif prevOp == '*':
        result = stack[-1] * crtNum
        stack.append(result)

      elif prevOp == '/':
        result = stack[-1] / crtNum
        stack.append(result)

      crtNum = 0
      prevOp = c