class Solution:
    def twoSum(self, nums, target):
        dict_nums = {}

        for i in range(len(nums)):
            dict_nums[nums[i]] = i
        
        for j in range(len(nums)):
            second_num = target - nums[j]
            if second_num in dict_nums.keys() and dict_nums[second_num] != j:
                return sorted([dict_nums[second_num], j])
                break