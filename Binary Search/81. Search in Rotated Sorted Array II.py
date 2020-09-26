# Similar to Search in a rotated sorted array without duplicates
class Solution:
  def search(self, nums: List[int], target: int) -> bool:
    if not nums:
      return False
    l, r = 0, len(nums) - 1

    while l + 1 < r:
      mid = (l + r) // 2
      if nums[mid] == target:
        return True
      # [1, 2, 2, 2]
			#     l  m  r
      while l < mid and nums[l] == nums[mid]:
        l += 1
      
      if nums[l] <= nums[mid]:
        if nums[l] <= target < nums[mid]:
          r = mid
        else:
          l = mid
      else:
        if nums[mid] <= target <= nums[r]:
          l = mid
        else:
          r = mid
      
    if nums[l] == target: return True
    if nums[r] == target: return True
    return False
