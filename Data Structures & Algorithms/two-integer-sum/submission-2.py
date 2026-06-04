class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
                nmap = {}
                for i, j in enumerate (nums):
                        rem = target - j
                        if rem in nmap:
                                return [nmap[rem], i]
                        nmap [j] = i