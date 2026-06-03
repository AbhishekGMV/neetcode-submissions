class Solution:
    def binarySearch(self, l, r, nums, target):
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        res = self.binarySearch(0, pivot-1, nums, target)
       
        if res != -1:
            return res
        return self.binarySearch(pivot, n-1, nums, target)