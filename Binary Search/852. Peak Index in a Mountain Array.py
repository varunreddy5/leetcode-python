class Solution:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    l, r = 0, len(arr) - 1
    while l + 1 < r:
      mid = (l + r) // 2
      # if arr[mid] > arr[mid + 1], then we can say that the right sub array has decreasing trend, so the peak exists in left sub array, so shift r = mid
      if arr[mid] > arr[mid + 1]:
        r = mid
      else:
        l = mid
    return l if arr[l] > arr[r] else r