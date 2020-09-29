# weights = [3,2,2,4,1,4], D = 3
# We can take a weight[i] on one day and can't be split, so the minimum weight it needs to carry a day is max(weights) and the maximum weight it can carry a day is sum(weights)
# Do a binary search with these as l and r
class Solution:
  def shipWithinDays(self, weights: List[int], D: int) -> int:
    l, r = max(weights), sum(weights)
    
    while l + 1 < r:
      mid = (l + r) // 2
      
      if self.calculateNumberOfDays(weights, mid) > D:
        l = mid
      else:
        r = mid
    if self.calculateNumberOfDays(weights, l) <= D:
      return l
    else:
      return r
  
  def calculateNumberOfDays(self, weights, K):
    num_of_days = 0
    _sum = 0
    for i in range(len(weights)):
      if _sum + weights[i] > K:
        num_of_days += 1
        _sum = weights[i]
      else:
        _sum += weights[i]
    if _sum:
      num_of_days += 1
    return num_of_days