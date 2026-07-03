class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        now = 1
        won = 1
        for i in range(len(nums)):
            left[i] = now
            now *= nums[i]
        for j in range(len(nums)-1,-1,-1):
            right[j] = won
            won *= nums[j]
        return [left[l]*right[l] for l in range(len(nums))]