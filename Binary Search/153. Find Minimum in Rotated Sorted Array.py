# Related problems:
# 33
# 81
class Solution:
  def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l + 1 < r:
      mid = (l + r) // 2
			
			# If the array is in sorted order, then return l
      if nums[l] < nums[r]:
        return nums[l]
			# If left array is sorted and the right is less than mid, then the minimum
			# is present in the right half
      if nums[l] < nums[mid]:
        if nums[mid] > nums[r]:
          l = mid
			# If right array is sorted and the left is greater than mid, then the minimum
			# is present in the left half
      else:
        if nums[l] > nums[mid]:
          r = mid
    return nums[l] if nums[l] < nums[r] else nums[r]