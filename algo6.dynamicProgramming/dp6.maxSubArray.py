# 53
# Kadane's Algorithm

# 문제: 주어진 Array에서 최대 Maximum Subarray를 계산하여라, 이때 서브어레이는 연속된 숫자로 이루어진 부분배열
# 이제까지 초급 문제들은 "주어진 문제의 솔루션이 일반적인 다이내믹 프로그래밍 스트럭쳐 프라블럼의 솔루션과 완벽히 같았다" 
# 즉 문제 그대로 풀면 되었다. 하지만 이 문제는 Maximum Subarray with last element 문제로 바꾸어야 한다.
# 만약 마지막 원소를 포함하지 않으면 상위 문제를 풀기 위해 하위문제의 솔루션을 사용해야하는 dp 가 되지 않기 때문임

# nums = [5,-2,9]
# dpArray = [5,5,12] 이 되는데 12를 알기위해 [5,-2]의 솔루션이 필요하지 않았고 오직 [5]의 솔루션만 필요했음 그래서 디피로 풀 수 없었음
# 그래서 dpArray = [5,3,12] 가 되도록 매 마지막 원소를 포함시킨 거임, 12가 되는 것은 똑같음

# F(n) = max(In(n), In(n)+F(n-1)) 의 점화식으로 정의 가능
# 이렇게 재정의하려면 n번째 부분배열최대합을 구할때, n번째 원소값을 무조건 포함한 maxSubArraySum을 구하는 문제로 재정의함

from typing import List

def maxSubArray(nums: List[int]) -> int:
  if len(nums) == 0:
    return 0

  if len(nums) == 1:
    return nums[0]

  dpArray = [0] * len(nums)
  dpArray[0] = nums[0]

  for idx in range(1, len(nums)):
    lastMaxSum = dpArray[idx-1]
    crtNum = nums[idx]

    crtMaxSum = max(crtNum, crtNum+lastMaxSum)    # 이전 하위문제(부분배열) 솔루션과 연결할지 아니면 지금 idx부터 새로운 부분배열을 시작할지 결정
    dpArray[idx] = crtMaxSum

  maxSubArraySum = max(dpArray)
  return maxSubArraySum

