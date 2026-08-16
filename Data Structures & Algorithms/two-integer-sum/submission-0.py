class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        empty_dict = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in empty_dict:
                return [empty_dict[diff], index]
            else:
                empty_dict[value] = index