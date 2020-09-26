# Similar questions:
# 35
class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    if not nums:
      return [-1, -1]
    # To find the first occurrence of the target
    first = self.binarySearch(nums, target, True)
    
    # To find the last occurrence of the target
    last = self.binarySearch(nums, target, False)
    return [first, last]
  
  def binarySearch(self, nums, target, pos):
    l, r = 0, len(nums) - 1
    while l + 1 < r:
      mid = (l + r) // 2
      
      # To find the first position, once the mid is equal to target, then we need to move the right pointer to mid
      if pos:
        if nums[mid] == target:
          r = mid
          continue
      # To find the last position, once the mid is equal to target, then we need to move the left pointer to mid
      else:
        if nums[mid] == target:
          l = mid
          continue
      # Normal binary search conditions
      if target > nums[mid]:
          l = mid
      else:
          r = mid
    # Once we are out of the loop, i.e., l + 1 < r, there might be a situation where nums[l] == target and nums[r] == target, then we need to return l
    if pos:
      if nums[l] == target: return l
      if nums[r] == target: return r
      return -1
    else:
      if nums[r] == target: return r
      if nums[l] == target: return l
      return -1