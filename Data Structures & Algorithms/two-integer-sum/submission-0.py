class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            s[i] = target - nums[i]
        
        for i in range(len(nums)):
            for key, val in s.items():
                if nums[i] == val and key != i:
                    return [i, key]