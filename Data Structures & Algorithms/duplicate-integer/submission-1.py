class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checking_list = set(nums)
        if len(checking_list) < len(nums):
            return True
        else:
            return False
        