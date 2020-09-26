# Related problems:
# 34
# 35
class Solution:
  def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    if not arr:
      return arr
		# Find the index of the element closest or equal to the target
    index = self.binarySearch(arr, x)
    l, r = index - 1, index + 1
    count = 1
    
		# From that index move one index to the left or right and capture the elements until the count >= k
    while count < k:
      if l < 0 and r < len(arr):
        r += 1
      elif l >= 0 and r >= len(arr):
        l -= 1
      else:
        if abs(arr[l] - x) <= abs(arr[r] - x):
          l -= 1
        else:
          r += 1
      count += 1
    return arr[l+1: r]
  
  def binarySearch(self, arr, target):
    l, r = 0, len(arr) - 1
    while l + 1 < r:
      mid = (l + r) // 2
      if arr[mid] == target:
        return mid
      if target > arr[mid]:
        l = mid
      else:
        r = mid
    return l if abs(arr[l] - target) <= abs(arr[r] - target) else r