class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        result = []
        lengthCountList = [[] for i in range(len(nums)+1)]
        for n in nums:
            res[n] = res.get(n,0)+1
        for n,c in res.items():
            lengthCountList[c].append(n)
        for i in range(len(lengthCountList)-1,0,-1):
            for n in lengthCountList[i]:
                result.append(n)
                if len(result) == k:
                    return result