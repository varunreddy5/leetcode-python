class Solution:
  def mySqrt(self, x: int) -> int:
	l, r = 1, x
	while l + 1 < r:
	  mid = (l + r) // 2
	  target = mid * mid
	  if target == x:
		return mid
	  if target > x:
		r = mid
	  else:
		l = mid
	  return l if x != 0 else 0