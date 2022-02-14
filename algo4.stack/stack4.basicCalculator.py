# 227
# 문자열로 주어진 계산을 숫자처럼 계산하기

# 요놈 어려움, 나중에 다시 보기

# 스택이 어려운 이는 포문과 함께 현재 순번과 이전 순번을 이용하고
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