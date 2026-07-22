class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sandra = set(nums)
        lstreak = 0
        
        for i in sandra:
            if i-1 not in sandra:
                cnum = i
                cstreak = 1
                while cnum+1 in sandra:
                    cnum += 1 
                    cstreak += 1
                lstreak = max(lstreak, cstreak)
        
        return lstreak

