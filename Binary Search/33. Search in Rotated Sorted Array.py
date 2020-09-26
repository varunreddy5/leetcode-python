class Solution:
  def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l + 1 < r:
      mid = (l + r) // 2
			
      if nums[mid] == target:
        return mid
			
			# if l < mid, then left array is sorted.
      if nums[l] <= nums[mid]:
				# Check if target is between l and mid
        if nums[l] <= target <= nums[mid]:
          r = mid
        else:
          l = mid
			
			# if mid < r, then right array is sorted.
      else:
				# Check if target is between mid and r
        if nums[mid] <= target <= nums[r]:
          l = mid
        else:
          r = mid
    if nums[l] == target: return l
    if nums[r] == target: return r   
    return -1