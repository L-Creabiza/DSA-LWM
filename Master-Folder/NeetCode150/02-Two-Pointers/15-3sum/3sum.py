class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i, j in enumerate(nums):
            if i>0 and j == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                threesum = j + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    result.append([j,nums[left],nums[right]]) 
                    left += 1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
        return result      