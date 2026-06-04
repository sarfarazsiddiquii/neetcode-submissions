class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapn = {}
        for i in nums:
            if i in mapn:
                mapn[i] += 1
            else:
                mapn[i] = 1
        return sorted(mapn, key=mapn.get, reverse=True)[:k]