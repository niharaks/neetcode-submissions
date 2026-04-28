class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for i in range(0, len(nums)):
            if nums[i] in a:
                return True
            else:
                a.add(nums[i])
        return False