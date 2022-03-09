# 155
# 문제: minimum값을 O(1) time complexity로 return이 가능한 Stack을 Design 하여라
# 이 스택에는 push, pop, top, max 함수가 제공되어야 함

# 맥스를 리턴하기 위해 반복문을 돌리면 O(n) 인데, 이거보다 나은 방법 찾아야함
# 기본스택과 맥스스택, 두개 이용하자. 이러면 SC 를 희생해서 TC를 빠르게 하는것, 트레이드오프 
# 새로운 값을 푸쉬하면, 그 값이 기존 값보다 큰 값이면 맥스 스택에 그 값을 푸쉬
# 이 새로운 값이 기존 값보다 작은 값이면 맥스스택에 원래 맨 위에 있는 맥스값을 다시 푸쉬, 이러면 맥스스택에 계속 맥스값을 탑에 유지할 수 있음
# 이렇게 하면 팝할때 두 스택을 함께 팝해줘야함

# 그런데 새로운 값을 푸쉬하면, 그 값이 기존 값보다 작은 값이면 맥스 스택에 그 값을 푸쉬할 필요 없이 걍 유지하면, 맥스스택의 탑이 그 스택의 최대값임
# 맥스값이 한번 더 푸쉬되면 맥스스택에 맥스값 한번더 푸쉬
# 이런 경우 팝을 할때, 기본스택의 팝한 값이 맥스스택의 탑 값보다 작으면 맥스스택은 팝하지 않고, 만약 이 두값이 같으면 두 스택 모두 팝해야함

# 최적화를 위해 맥스값이 한번 더 푸쉬되면 맥스스택에 맥스값 한번더 푸쉬하는 것이 아니라
# (maxValue, 2) 이런식으로 스택에 쌓을 수 있음
# 그러나 이는 시간복잡도가 동일하게 O(1) 임

# 포인트는 맥스값 찾는 것을 O(1)으로 유지하는 것임, 이를 위해 맥스스택 탑을 기본스택의 맥스값으로 유지
# 미니멈스택과 맥시멈스택은 결국 똑같은 구조임




from typing import List  

class MinStack:
  def __init__(self):
    self._stack = []
    self._min_stack = []

  def push(self, val: int) -> None:
    if len(self._stack) == 0:
      self._stack.append(val)
      self._min_stack.append(val)
      return
    
    min_num = self._min_stack[-1]
    if val < min_num:
      self._stack.append(val)
      self._min_stack.append(val)
      
    else:
      self._stack.append(val)
      self._min_stack.append(min_num)    


  def pop(self) -> None:
    if len(self._stack) != 0:
      self._stack.pop()
      self._min_stack.pop()
    

  def top(self) -> int:
    return self._stack[-1]

  def getMin(self) -> int:
    return self._min_stack[-1]
        

minStack = MinStack()
minStack.push(5)
print(minStack.getMin(),end=' ')
minStack.push(3)
print(minStack.getMin(),end=' ')
minStack.push(2)
print(minStack.getMin(),end=' ')
minStack.push(4)
print(minStack.getMin(),end=' ')
minStack.pop()
minStack.pop()
print(minStack.getMin(),end=' ')




#################################################################



class MaxStack:
  def __init__(self):
    self.stack = []
    self.maxStack = []


  def push(self, val: int) -> None:
    if len(self.stack) == 0:
      self.stack.append(val)
      self.maxStack.append(val)

    maxNum = self.maxStack[-1]
    if val < maxNum:
      self.stack.append(val)
      self.maxStack.append(maxNum)

    else:
      self.stack.append(val)
      self.maxStack.append(val)


  def pop(self) -> None:
    self.stack.pop()
    self.maxStack.pop()


  def top(self) -> int:
    return self.stack[-1]

  def max(self) -> int:
    return self.maxStack[-1]

