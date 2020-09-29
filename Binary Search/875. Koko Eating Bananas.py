# piles = [3,6,7,11], H = 8
# So basically you can eat minimum of one pile an hour or maximum of max(piles) an hour
# So we start with l = 1 and r = max(piles) -> 11. Also, assume H >= len(piles)
# If Koko eats 11 piles an hour, H = 4
# If Koko eats 1 + 11 / 2 = 6 then it can complete in 6 hours
import math
class Solution:
  def minEatingSpeed(self, piles: List[int], H: int) -> int:
    l, r = 1, max(piles)
    while l + 1 < r:
      mid = (l + r) // 2
      if self.calculateNumOfHours(piles, mid) > H:
        l = mid
      else:
        r = mid
		#If the calculatedHours <= H, finally, then we need to return l. Else r
    if self.calculateNumOfHours(piles, l) <= H: 
      return l
    else:
      return r
    
  
  def calculateNumOfHours(self, piles, K):
    num_of_hours = 0
    for pile in piles:
      num_of_hours += math.ceil(pile / K)
    return num_of_hours