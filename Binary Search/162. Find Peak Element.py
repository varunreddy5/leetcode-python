class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l + 1 < r:
      mid = (l + r) // 2
			# check if nums[mid] < numd[mid + 1], it means that the current mid has an increasing sequqnce and there is a possibility that the element is present between [mid, r] 
      if nums[mid] > nums[mid + 1]:
        r = mid
      else:
        l = mid
    return l if nums[l] > nums[r] else r