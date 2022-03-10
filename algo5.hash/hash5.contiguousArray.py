# 문제: 1과 0으로 이루어진 array에서 1과 0의 갯수가 같은 subarray의 최대길이는 몇 인가?

# two pointers 로 풀기 어려운 이유는 어떤 조건에 포인터를 움직여줘야 하는지 정하기 어려움
# 이전 문제와 마찬가지로 누적합과 해쉬테이블을 이용, 
# 시간복잡도 O(n) 공간복잡도 O(n)

# 포인트는 1, 0인 애들이 입력값으로 들어오기에, 0을 -1로 치환해서 누적을 이용하는것, 갯수가 같으면 전체 합이 0이 됨
# 입력값이 알파벳이라도 치환할 수 있음

# 포인트는 누적값의 부분배열의 합은, 누적값에서 구하고자하는 부분배열 이전까지의 누적값을 빼주면 된다는 것.


from typing import List

def findMaxLength(nums: List[int]) -> int:
    
    for idx in range(len(nums)):
      if nums[idx] == 0 :
        nums[idx] = -1
        
    cml_sums = []
    tmp_sum = 0
    for num in nums:
      tmp_sum += num
      cml_sums.append(tmp_sum)
    
    table = {}
    max_length = 0
    table[0] = [-1]
    
    for idx, cml_sum in enumerate(cml_sums):
      if cml_sum not in table:
        table[cml_sum] = [idx]
      else:
        table[cml_sum].append(idx)
        
      indices = table[cml_sum]
      first_idx = indices[0]
      last_idx = indices[-1]
      length = last_idx - first_idx
      max_length = max(max_length,length)
      
    return max_length

findMaxLength(nums=[1,0,1,1,1,0,0,1,1])


##################################################


def contigArray(nums: List[int]) -> int:
  
  for idx, num in enumerate(nums):
    if num == 0:
      nums[idx] = -1

  accumNums = []
  tempNum = 0
  for num in nums:
    tempNum += num
    accumNums.append(tempNum)

  maxLength = 0
  hashTable = {}
  hashTable[0] = [-1]       # 배열의 0번째에서부터 n번째가 해당하는 부분 배열이라면 이 배열의 길이를 구하기 위해 배열의 -1번째 값을 0으로 둔다는 뜻으로, 해시테이블에 입력
                                                  # 포인트는 누적값의 부분배열의 합은, 누적값에서 구하고자하는 부분배열 이전까지의 누적값(target)을 빼주면 된다는 것. 따라서 여기서는 누적값의 부분배열의 합이 0인 부분배열을 구하는 것
                                                  # accNum - target = sum
  for idx, accumNum in enumerate(accumNums):      # 해시테이블에는 같은 누적수의 인덱스들이 오름차순 배열로 들어가게 됨. target = accNum - sum, sum = 0 이기 때문에, target = accNum, 누적값이 target이라 다음 누적값을 찾으면됨
    if accumNum not in hashTable:
      hashTable[accumNum] = [idx]             # 해쉬테이블에 누적값이 같은 인덱스들만 배열로 저장
    else:
      hashTable[accumNum].append(idx)         # target = accNum - sum, sum = 0 이기 때문에, target = accNum, 누적값이 target이라 다음 누적값을 찾으면됨

    startIdx = hashTable[accumNum][0]           
    endIdx = hashTable[accumNum][-1]
    lenth = endIdx - startIdx             # 0~startIdx까지 누적값 == 0~endIdx 누적값 같으므로, 0~endIdx 누적값에서 0~startIdx까지 누적값을빼면 startIdx+1 ~ endIdx 합이 0이라는 뜻, 그 0이되는 부분배열의 길이가 두 인덱스의 차, 구하고자하는 부분배열 이전까지의 누적값(target)을 빼주면 된다는 것, 
    maxLength = max(maxLength, lenth)     # 최대길이를 구하는 문제이므로 그 길이를 맥스함수로. 다만 반복문을 수행할수록 그 길이는 업데이트 될 것임.

  return maxLength

