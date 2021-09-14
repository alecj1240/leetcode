class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for pointer in range(len(nums)):
            goal = target - nums[pointer]
            if goal in nums:
                if nums.index(goal) != pointer:
                    return [pointer, nums.index(goal)]
