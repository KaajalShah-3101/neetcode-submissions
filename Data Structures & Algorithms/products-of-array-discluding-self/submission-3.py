class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initializing prefix and suffix array with zero as a placeholder for now
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        final = [0] * n

        # first element of pre and last element of suf equaled to 1 
        pre[0], suf[n-1] = 1, 1
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        for i in range(n):
            final[i] = pre[i] * suf[i]
        return final

        