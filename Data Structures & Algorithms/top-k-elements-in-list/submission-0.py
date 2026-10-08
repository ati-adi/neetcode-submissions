class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}

        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1
        
        sorted_dict = sorted(dict_nums, key=dict_nums.get, reverse=True)

        return sorted_dict[:k]