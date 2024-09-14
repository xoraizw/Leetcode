class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for x in range(len(nums) - 2):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            l, r = x + 1, len(nums) - 1
            while l < r:
                total = nums[x] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[x], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res
