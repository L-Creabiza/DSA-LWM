class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dick = {}
        for i in strs:
            key = tuple(sorted(i))
            if key in dick:
                dick[key].append(i)
            else:
                dick[key] = [i] 
        return list(dick.values())

        