# unstable
# 숫자들을 카운팅해서 정렬을 하기 때문에 counting sort
# 좋은 문제는 아님
# O(n + k)

from typing import List

def countingSort(nums: List[int]) -> List:
   minNum = min(nums)
   maxNum = max(nums)
   
   range = maxNum - minNum + 1          # 최대값에서 최소값을 빼준 만큼 리스트를 생성하기에, 이값이 너무 크면 k 가 커지고 느린 알고리즘이 됨
   counts = [0] * range                 # 다만 알파벳 같이 한정된 갯수가 있다면 빠름

   for num in nums:                 # counts 리스트에 각 숫자의 갯수를 넣어줌. 즉 인덱스가 해당숫자고 값이 그 숫자의 갯수
     idx = num - minNum
     counts[idx] += 1

  
   accumCounts = []
   accum = 0
   for count in counts:             # 그 후 그 숫자의 갯수들을 왼쪽에서 오른쪽을 더하면서 누적, 그러면 그 값들이 해당 인덱스(정렬할 수)의 위치값이 됨 
      accum += count
      accumCounts.append(accum)

   newAccumCounts = [a-1 for a in accumCounts]   # 하지만 갯수니까 인덱스를 나타내려면 -1 해줘야함
   
   results = [0] * len(nums)
   for num in reversed(nums):       
     countIdx = num - minNum        # countIdx는 정렬하고자하는 숫자값
     idx = newAccumCounts[countIdx]  # 이 숫자값이 newAccumCounts의 인덱스 값으로 인덱싱해주면 정렬될 위치 인덱스가 나옴
     results[idx] = num
     newAccumCounts[num] -= 1

   
   return results

print(countingSort(nums=[3,4,0,1,2]))