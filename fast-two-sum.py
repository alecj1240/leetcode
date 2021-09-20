class Solution:
    def twoSum(self, nums, target):
        number_bonds = {}
        for index, value in enumerate(nums):
            if value in number_bonds:
                return [number_bonds[value], index]
            number_bonds[target - value] = index
        return None

