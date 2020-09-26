# Similar questions:
# 34
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l + 1 < r:
      mid = (l + r) // 2
      
      if nums[mid] == target:
        return mid
      if target > nums[mid]:
        l = mid
      else:
        r = mid
    # Similar problem to finding the first position or last position in an array
    # If the target is less than l return l
    if target < nums[l]: return l
    if target > nums[r]: return r + 1
    # if the target is between l and r return r
    return r