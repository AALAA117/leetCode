class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                res = nums[a] + nums[b]
                if res == target:
                    return([a, b])
