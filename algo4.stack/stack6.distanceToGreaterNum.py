# 739
# 문제: 날짜에 따른 온도가 temperatures 리스트로 주어진다. 이 때 해당 날짜에서부터 다음 따뜻한날까지의 차이를 가진 list를 return하여라

# 배열에서 현재 인덱스가 가리키는 값보다 큰 다음 인덱스가 가리키는 수와의 거리, 즉 인덱스들 끼리의 차를 각 배열의 인덱스마다 구해서 배열로 리턴
# [39, 20, 70, 36, 30, 60, 80, 1]
# [ 2,  1,  4,  2,  1,  1,  0, 0]
# 끝에서 반대 방향으로 스택을 이용해서 진행해보자
# [(80, 6), (60, 5), (30, 4)] : 뒤에서 30까지 이렇게 스택이 쌓임, 3인덱스의 값이 36이고 이는 바로 전 30보다 크기 때문에, 36보다 큰 값이 나올 때까지 팝하면
# [(80, 6), (60, 5)] : 이렇게 되고
# [(80, 6), (60, 5), (36, 3)] : 새로 (36, 3)을 넣어줌, 다음 값 70때문에
# [(80, 6), (70, 2)]
# [(80, 6), (70, 2), (20, 1)]
# [(80, 6), (70, 2), (39, 0)]

# 날자에 따른 온도가 temperatures 리스트로 주어진다. 이 때 해당 날짜에서부터 다음 따뜻한날까지의 차이를 가진 list를 return하여라

# brute force 방법은 두 포인터를 이용하고 시간복잡도 O(n*n), 왼쪽에서 오른쪽으로 진행함
# 스택을 이용하면 O(n)으로 할 수 있고 이때 배열의 끝에서 왼쪽으로 진행함

# for 문 안에 while 문이 있다보니가 시간복잡도 O(n*n) 이라고 착각할 수 있는데 와일문은 스택을 이용하고 있고 스택의 최상단 값만 이용하고 있으므로 O(n)으로 볼 수 있음
# 공간복잡도는 스택의 O(n)


from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    temp_count = len(temperatures)
    ans = [0]*temp_count
    
    stack = []
    idx_stack = []
    
    for idx in range(temp_count-1,-1,-1):
      temperature = temperatures[idx]
      
      last_temp_idx = 0
      while stack:
        last_temp = stack[-1]
        last_temp_idx = idx_stack[-1]
        if last_temp <= temperature:
          stack.pop()
          idx_stack.pop()
        else:
          break
      
      if len(stack) == 0:
        stack.append(temperature)
        idx_stack.append(idx)
        ans[idx] = 0
        continue
        
      stack.append(temperature)
      idx_stack.append(idx)
      ans[idx] = last_temp_idx-idx
    
    return ans


dailyTemperatures(temperatures=[39, 20, 70, 36, 30, 60, 80, 1])




################################################################
# 배열에서 현재 인덱스가 가리키는 값보다 큰 다음 인덱스가 가리키는 수와의 거리, 즉 인덱스들 끼리의 차를 각 배열의 인덱스마다 구해서 배열로 리턴
# [39, 20, 70, 36, 30, 60, 80, 1]
# [ 2,  1,  4,  2,  1,  1,  0, 0]
# 끝에서 반대 방향으로 스택을 이용해서 진행해보자
# [(80, 6), (60, 5), (30, 4)] : 뒤에서 30까지 이렇게 스택이 쌓임, 3인덱스의 값이 36이고 이는 바로 전 30보다 크기 때문에, 36보다 큰 값이 나올 때까지 팝하면
# [(80, 6), (60, 5)] : 이렇게 되고
# [(80, 6), (60, 5), (36, 3)] : 새로 (36, 3)을 넣어줌, 다음 값 70때문에
# [(80, 6), (70, 2)]
# [(80, 6), (70, 2), (20, 1)]
# [(80, 6), (70, 2), (39, 0)]



def distanceToGreaterNumer(nums: List[int]) -> List[int]:
  count = len(nums)
  results = [0] * count

  numStack = []                   # 숫자, 인덱스 각각 두개의 스택
  idxStack = []

  for idx in range(count-1, -1, -1):
    num = nums[idx]

    lastIdx = 0
    while numStack:             # 숫자 스택은 이전 숫자들이 있기 때문에 현재수와 비교해서 현재수 보다 작은 애들을 팝해주고
      lastNum = numStack[-1]    # 현재 수보다 큰 애를 만나면 브레이크
      lastIdx = idxStack[-1]    # while 문에서 idxStack에서 남은, 즉 현재 수보다 큰 수가 있는 인덱스, results에 들어갈 값을 위해 필요, while문 안의 변수인데 바깥에서 쓸수 있다고??
                                # 팝하고 난 후에 만약 numStack, idxStack이 팝으로 빈배열만 남으면, 밑에서 lastIdx를 알길이 없으므로 여기에 미리 적어두는 거임
      if num > lastNum:         # 빈배열이 아닌데 while을 탈출하는 경우는 현재 수가 lastNum 보다 작을 경우이고 이 때는 lastIdx를 인덱스 스택에서 접근해서 알 수 있음
        numStack.pop()
        idxStack.pop()
      else:
        break                   # 현재수가 오른쪽 수보다 작으면 while 반복문 탈출하고 지금 값과 인덱스 스택에 넣어줌

    if len(numStack) == 0:      # len(numStack) == 0, 즉 스택이 비어있으면 스택에 현재 값들 넣어주고 다음 반복문으로 continue
      results[idx] = 0          # 스택이 비어있다는 것은 해당 인덱스의 오른쪽으로 더 큰 수가 없다는 뜻
      numStack.append(num)
      idxStack.append(idx)
      continue                  # continue는 밑에 로직 실행 안하고 포문의 다음 순번을 처리하라는 뜻

     
    results[idx] = lastIdx - idx  # len(numStack) == 0, 즉 스택이 비어있으면 해당 과정 이하를 실행하지 않음. 스택이 비어있다는 것은 해당 인덱스의 오른쪽으로 더 큰 수가 없다는 뜻이고, 이는 값이 0이라는 의미
    numStack.append(num)
    idxStack.append(idx)

  return results

distanceToGreaterNumer([39, 20, 70, 36, 30, 60, 80, 1])