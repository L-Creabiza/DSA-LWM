class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tally = Counter(nums)
        return [item for item, count in tally.most_common(k)]
