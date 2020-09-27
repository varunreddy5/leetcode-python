# Combination of find minimum in rotated sorted array
class Solution:
  def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    
    while l + 1 < r:
      mid = (l + r) // 2
      
			# if the left element is less than right element, then the array is sorted, then return the leftmost element
      if nums[l] < nums[r]:
        return nums[l]
      
			# If the left element is equal to mid then increment the left index
      while l < mid and nums[l] == nums[mid]:
        l += 1
      
			# If the left sub array is sorted
      if nums[l] <= nums[mid]:
				# Check if mid element is greater than than right, if so the minimum is present in the right sub array
        if nums[mid] > nums[r]:
          l = mid
			# If right sub array is sorted
      else:
				# Check if left element is greater than than mid, if so the minimum is present in the left sub array
        if nums[l] > nums[mid]:
          r = mid
    return nums[l] if nums[l] < nums[r] else nums[r]