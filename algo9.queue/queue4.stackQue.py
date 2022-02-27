class Queue:
  def __init__(self):
    self._pushStack = []
    self._popStack = []

  def enque(self, x: int) -> None:
    self._pushStack.append(x)

  def deque(self) -> int:
    if len(self._popStack) > 0:
      self._popStack.pop()

    self.moveToPopStack()
    return self._popStack.pop()


  def moveToPopStack(self):
    while self._pushStack:
      tempVal = self._pushStack.pop()
      self._popStack.append(tempVal)