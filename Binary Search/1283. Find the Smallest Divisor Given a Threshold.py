# Related Leetcode problems:
#
import math
class Solution:
  def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    # Take the highest number in the array as r and l as 1
    l, r = 1, nums[-1]
    while l + 1 < r:
      mid = (l + r) // 2
			# calculate the mid and check if sum of the quotients of mid is less than threshold
			# if True, then make  r = mid
      if self.sumOfQuotients(nums, mid, threshold):
        r = mid
      else:
        l = mid
    if self.sumOfQuotients(nums, l, threshold): return l
    if self.sumOfQuotients(nums, r, threshold): return r 
  
  def sumOfQuotients(self, arr, num, threshold):
    _sum = 0
    for i in arr:
      _sum += math.ceil(i / num)
    return _sum <= threshold