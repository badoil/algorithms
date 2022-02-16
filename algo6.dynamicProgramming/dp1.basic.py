# dp는 3가지 조건 충족되야함
# 1. 문제가 하위문제로 쪼개질 수 있는가
# 2. 이 하위문제의 솔루션으로 상위문제의 솔루션을 구할 수 있는가
# 3. 이 하위문제들이 중복되는가(중복되면 기억해(memozation) 놓았다가 한번만 풀고 필요할때 쓰면됨)

# dp 는 결국 문제와 하위문제를 정의하는 것이 관건이고 그건 문제를 많이 풀어야함

# 대표적으로 피보나치 수열

# 메모이제이션 안쓴 함수
# 속도가 느림
def bruteForceFibo(num: int) -> int:
  if num == 0:
    return 0
  elif num == 1:
    return 1

  fibo = bruteForceFibo(num-1) + bruteForceFibo(n-2)
  return fibo

# 재귀와 메모이제이션
# 이 놈은 위에 것보다 빠르지만
# num이 커지면 overstackflow 발생
# num < len(memos) 순간까지 재귀 스택이 쌓이게됨
# 즉 fibo(2) = recurMemoFibo(1) + recurMemoFibo(0) 까지 가게됨.
# 이것은 fibo(num)에서 시작하는 탑-다운 방식임
# 오버스택플로우 문제 때문에 바텀-업 방식을 찾아야함
memos = [0, 1 ]
def recurMemoFibo(num: int) -> int:
  if num < len(memos):
    return memos[num]

  fibo = recurMemoFibo(num-1) + recurMemoFibo(num-2)
  return fibo


# 바텀-업
# 시간복잡도 O(n), 공간복잡도 O(n)
def iterMemoFibo(num: int) -> int:
  if num ==0:
    return 0 
  elif num == 1:
    return 1

  dpArray = [0, 1]
  for i in range(2, num+1):
    fibo = dpArray[i-2] + dpArray[i-1]
    dpArray.append(fibo)
  
  return dpArray[num]

