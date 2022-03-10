# 문제: 주어진 point들로 만들수 있는 직사각형중 최소 size는 몇인가?

from typing import List  
import sys

def minAreaRect(points: List[List[int]]) -> int:
  table = {}
  for point in points:
    x = point[0]
    y = point[1]
    if x not in table:
      table[x] = set()        
    table[x].add(y)
    
  min_area = sys.maxsize
  
  for first_idx in range(len(points)):
    first_pt = points[first_idx]
    px0 = first_pt[0]
    py0 = first_pt[1]
    for second_idx in range(first_idx+1,len(points)):
      second_pt = points[second_idx]
      px1 = second_pt[0]
      py1 = second_pt[1]
      
      expected_area = abs(px0-px1) * abs(py0-py1)
      if expected_area == 0:
        continue
      
      pt2 = (px0,py1)
      pt3 = (px1,py0)
      
      set2 = table[pt2[0]]
      if pt2[1] not in set2:
        continue
        
      set3 = table[pt3[0]]
      if pt3[1] not in set3:
        continue
      
      min_area = min(min_area, expected_area)
  
  if min_area==sys.maxsize:
    min_area = 0
    
  return min_area
      
minAreaRect(points=[(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1)])



##########################################################################