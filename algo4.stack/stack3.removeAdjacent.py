# 1047
# 문제: string 에서 같은 두개의 연속된 알파벳들을 제거하여라 
# 문자열안에 2개 알파벳 있으면 지워주기


def removeDuplicates(string: str) -> str:
  stack = []
  for c in string:
    if len(stack) != 0 and c == stack[-1]:
      stack.pop()
    else:
      stack.append(c)

  return ','.join(stack)
print(removeDuplicates('abbcbbcdef'))



# 1209
# 알파벳이 k개 연속으로 나오면 해당 문자열을 지워주기


def removeDuplicates2(s: str, k: int) -> str:
  stack = []
  count_stack = []
  
  for c in s:
    if len(stack) == 0:
      stack.append(c)
      count_stack.append(1)
          
    elif stack[-1] == c:
      dup_count = count_stack[-1]
      if dup_count < k-1:
        stack.append(c)
        count_stack.append(dup_count+1)
      elif dup_count == k-1:            # dup_count가 k-1이면 현재 k번 연속으로 나왔다는 뜻임
        for _ in range(k-1):
          stack.pop()
          count_stack.pop()
      
    else:
      stack.append(c)
      count_stack.append(1)

  return ''.join(stack)

print(removeDuplicates2(s='abbcddde',k=3))




###########################################################################




def removeDuplicatesK(string: str, k: int) -> str:
  stack = []
  countStack = []

  for c in string:
    if len(stack) == 0:
      stack.append(c)
      countStack.append(1)

    elif c == stack[-1]:
      if countStack[-1] < k-1:
        count = countStack[-1]
        stack.append(c)
        countStack.append(count+1)

      elif countStack[-1] == k-1:
        count = countStack[-1]
        for _ in range(count):
          stack.pop()
          countStack.pop()

    else:
      stack.append(c)
      countStack.append(1)
